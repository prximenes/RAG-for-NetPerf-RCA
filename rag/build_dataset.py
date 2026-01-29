#!/usr/bin/env python3
"""
Script independente para construir o dataset do RAG (Qdrant embedded).

Baseado no `rag-application/dataset/build_dataset.py`, ajustado para este artefato:
- Usa `./qdrant_storage` como destino padrão (na raiz do repositório)
"""

# NOTE: este arquivo foi copiado do projeto principal para manter o artefato autocontido.

import argparse
import json
import logging
from pathlib import Path
from typing import List, Dict, Any
import uuid
import hashlib
from datetime import datetime
import os

try:
    from rag.text_cleaner import TextCleaner  # type: ignore
except Exception:  # pragma: no cover
    TextCleaner = None  # type: ignore

try:
    from qdrant_client import QdrantClient
    from qdrant_client.models import VectorParams, Distance, PointStruct
    from llama_index.readers.file import PDFReader
    from llama_index.core.node_parser import SentenceSplitter
    from transformers import AutoModel, AutoTokenizer
    import torch
    import torch.nn.functional as F
except ImportError as e:
    print(f"Erro ao importar dependências: {e}")
    print("\nInstale as dependências necessárias:")
    print("   uv sync")
    raise SystemExit(1)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

EMBED_DIM = 1024
COLLECTION_NAME = "docs"


class EmbeddingModel:
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.device = None

    def load(self):
        if self.model is not None:
            return

        logger.info("Carregando Qwen3-Embedding-0.6B...")
        self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-Embedding-0.6B")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = AutoModel.from_pretrained(
            "Qwen/Qwen3-Embedding-0.6B",
            dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto" if torch.cuda.is_available() else None,
        )
        self.model.eval()
        logger.info("Modelo carregado! Dimensão=%s | device=%s", EMBED_DIM, self.device)

    def embed_texts(self, texts: List[str], batch_size: int = 8) -> List[List[float]]:
        if self.model is None:
            self.load()

        embeddings: List[List[float]] = []
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            inputs = self.tokenizer(  # type: ignore
                batch,
                padding=True,
                truncation=True,
                max_length=512,
                return_tensors="pt",
            )
            if torch.cuda.is_available():
                inputs = {k: v.to(self.model.device) for k, v in inputs.items()}  # pyright: ignore

            with torch.no_grad():
                outputs = self.model(**inputs)  # pyright: ignore
                attention_mask = inputs["attention_mask"]
                token_embeddings = outputs.last_hidden_state
                input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
                sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
                sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
                batch_embeddings = sum_embeddings / sum_mask
                batch_embeddings = F.normalize(batch_embeddings, p=2, dim=1)
                embeddings.extend(batch_embeddings.cpu().float().tolist())

        return embeddings


def chunk_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[str]:
    chunks: List[str] = []
    step = max(1, chunk_size - chunk_overlap)
    for i in range(0, len(text), step):
        chunk = text[i : i + chunk_size]
        if chunk.strip():
            chunks.append(chunk)
    return chunks


class QdrantStorage:
    def __init__(self, path: str, collection: str = COLLECTION_NAME):
        self.client = QdrantClient(path=path)
        self.collection = collection
        if not self.client.collection_exists(self.collection):
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(size=EMBED_DIM, distance=Distance.COSINE),
            )

    def clear_collection(self):
        if self.client.collection_exists(self.collection):
            self.client.delete_collection(self.collection)
        self.client.create_collection(
            collection_name=self.collection,
            vectors_config=VectorParams(size=EMBED_DIM, distance=Distance.COSINE),
        )


class DatasetBuilder:
    def __init__(
        self,
        dataset_dir: str = ".",
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        web_include_dirs: List[str] | None = None,
        web_exclude_dirs: List[str] | None = None,
        clean_text: bool = True,
        clean_aggressive: bool = False,
        clean_min_line_length: int = 0,
    ):
        self.dataset_dir = Path(dataset_dir)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.storage = QdrantStorage(path=str(self.dataset_dir / "qdrant_storage"))
        self.embedding_model = EmbeddingModel()
        self.processed_hashes = self._load_processed_hashes()
        self.web_include_dirs = web_include_dirs or []
        self.web_exclude_dirs = web_exclude_dirs or []
        self.clean_text_enabled = bool(clean_text)

        self.text_cleaner = None
        if self.clean_text_enabled and TextCleaner is not None:
            self.text_cleaner = TextCleaner(
                aggressive=bool(clean_aggressive),
                remove_line_breaks=True,
                fix_hyphenation=True,
                remove_page_numbers=True,
                remove_headers_footers=True,
                normalize_whitespace=True,
                normalize_punctuation=True,
                remove_control_chars=True,
                min_line_length=int(clean_min_line_length or 0),
                preserve_urls=True,
                preserve_emails=True,
                verbose=False,
            )

    def _load_processed_hashes(self) -> Dict[str, str]:
        hash_file = self.dataset_dir / ".processed_hashes.json"
        if hash_file.exists():
            return json.loads(hash_file.read_text(encoding="utf-8"))
        return {}

    def _save_processed_hashes(self):
        hash_file = self.dataset_dir / ".processed_hashes.json"
        hash_file.write_text(json.dumps(self.processed_hashes, indent=2), encoding="utf-8")

    def _file_hash(self, file_path: Path) -> str:
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def _maybe_clean(self, text: str) -> str:
        if not text:
            return text
        if not self.clean_text_enabled or self.text_cleaner is None:
            return text
        try:
            return self.text_cleaner.clean(text)
        except Exception as e:
            logger.warning("Falha ao limpar texto (continuando sem limpeza): %s", e)
            return text

    def _iter_files(self, root: Path, exts: set[str], ignore_dirs: set[str], max_bytes: int = 5_000_000) -> List[Path]:
        out: List[Path] = []
        if not root.exists():
            return out
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
            for fn in filenames:
                p = Path(dirpath) / fn
                if not p.is_file():
                    continue
                if max_bytes > 0:
                    try:
                        if p.stat().st_size > max_bytes:
                            continue
                    except OSError:
                        continue
                if p.suffix.lower() in exts:
                    out.append(p)
        return out

    def _process_text_file(self, file_path: Path, source_type: str, incremental: bool) -> List[Dict[str, Any]]:
        file_hash = self._file_hash(file_path)
        if incremental and self.processed_hashes.get(str(file_path)) == file_hash:
            return []

        text = file_path.read_text(encoding="utf-8", errors="replace")
        text = self._maybe_clean(text)
        chunks = chunk_text(text, self.chunk_size, self.chunk_overlap)
        embeddings = self.embedding_model.embed_texts(chunks)

        # ID determinístico baseado em caminho relativo (evita colisões)
        try:
            rel = file_path.relative_to(self.dataset_dir).as_posix()
        except Exception:
            rel = str(file_path)
        source_id = rel

        points = []
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            point_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"{source_id}:{i}"))
            payload = {
                "text": chunk,
                "source": file_path.name,
                "source_path": rel,
                "source_type": source_type,
                "chunk_index": i,
                "total_chunks": len(chunks),
                "processed_at": datetime.now().isoformat(),
            }
            points.append({"id": point_id, "vector": embedding, "payload": payload})

        self.processed_hashes[str(file_path)] = file_hash
        return points

    def build(self, incremental: bool = False, clear_existing: bool = False) -> int:
        logger.info("Iniciando build do dataset (dir=%s)", self.dataset_dir)

        if clear_existing and not incremental:
            logger.warning("Limpando coleção existente...")
            self.storage.clear_collection()
            self.processed_hashes = {}

        all_points: List[Dict[str, Any]] = []

        # PDFs (opcional): ./data/pdf ou ./data/pdfs
        pdf_dir = self.dataset_dir / "data" / "pdf"
        if not pdf_dir.exists():
            pdf_dir = self.dataset_dir / "data" / "pdfs"

        if pdf_dir.exists():
            reader = PDFReader()
            splitter = SentenceSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
            for pdf_file in sorted(pdf_dir.glob("*.pdf")):
                file_hash = self._file_hash(pdf_file)
                if incremental and self.processed_hashes.get(str(pdf_file)) == file_hash:
                    continue
                docs = reader.load_data(file=str(pdf_file))
                raw_text = "\n\n".join(d.text for d in docs if getattr(d, "text", None))
                cleaned = self._maybe_clean(raw_text)
                chunks = splitter.split_text(cleaned) if cleaned.strip() else []
                embeddings = self.embedding_model.embed_texts(chunks)
                rel = pdf_file.relative_to(self.dataset_dir).as_posix()
                for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
                    point_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"{rel}:{i}"))
                    all_points.append(
                        {
                            "id": point_id,
                            "vector": embedding,
                            "payload": {
                                "text": chunk,
                                "source": pdf_file.name,
                                "source_path": rel,
                                "source_type": "pdf",
                                "chunk_index": i,
                                "total_chunks": len(chunks),
                                "processed_at": datetime.now().isoformat(),
                            },
                        }
                    )
                self.processed_hashes[str(pdf_file)] = file_hash

        # Textos/KB: por padrão, este artefato usa `./kb_sample/`
        web_dir = self.dataset_dir / "kb_sample"
        if web_dir.exists():
            roots = [web_dir / d for d in self.web_include_dirs] if self.web_include_dirs else [web_dir]
            ignore_dirs = {"__pycache__", ".git", ".svn", "_build", "build", "_static", "img", "images"}
            exts = {".md", ".markdown", ".txt", ".rst", ".ini", ".cfg", ".conf"}

            files: List[Path] = []
            for r in roots:
                files.extend(self._iter_files(r, exts=exts, ignore_dirs=ignore_dirs, max_bytes=5_000_000))

            if self.web_exclude_dirs:
                excluded = set(self.web_exclude_dirs)

                def keep(p: Path) -> bool:
                    try:
                        rel = p.relative_to(web_dir)
                    except ValueError:
                        return True
                    return not rel.parts or rel.parts[0] not in excluded

                files = [p for p in files if keep(p)]

            for f in sorted(set(files)):
                st = f.suffix.lower().lstrip(".") or "text"
                all_points.extend(self._process_text_file(f, source_type=st, incremental=incremental))

        if all_points:
            logger.info("Inserindo %s chunks...", len(all_points))
            batch_size = 100
            for i in range(0, len(all_points), batch_size):
                batch = all_points[i : i + batch_size]
                point_structs = [
                    PointStruct(id=p["id"], vector=p["vector"], payload=p["payload"]) for p in batch
                ]
                self.storage.client.upsert(collection_name=self.storage.collection, points=point_structs)
                logger.info("Inseridos: %s/%s", min(i + batch_size, len(all_points)), len(all_points))

            self._save_processed_hashes()
            logger.info("Build finalizado. Total chunks inseridos=%s", len(all_points))
        else:
            logger.info("Nenhum documento novo para processar.")

        return len(all_points)

    def stats(self):
        info = self.storage.client.get_collection(self.storage.collection)
        logger.info("Estatísticas do Dataset:")
        logger.info("  Total chunks: %s", info.points_count)
        logger.info("  Dimensão embeddings: %s", info.config.params.vectors.size)
        logger.info("  Distância: %s", info.config.params.vectors.distance)


def main():
    parser = argparse.ArgumentParser(description="Build RAG dataset (Qdrant embedded)")
    parser.add_argument("--dataset-dir", default=".", help="Pasta base do artefato (padrão: .)")
    parser.add_argument("--chunk-size", type=int, default=1000)
    parser.add_argument("--overlap", type=int, default=200)
    parser.add_argument("--incremental", action="store_true")
    parser.add_argument("--clear", action="store_true")
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--web-include-dirs", nargs="*", default=[])
    parser.add_argument("--web-exclude-dirs", nargs="*", default=[])
    parser.add_argument("--no-clean", action="store_true")
    parser.add_argument("--clean-aggressive", action="store_true")
    parser.add_argument("--clean-min-line-length", type=int, default=0)
    args = parser.parse_args()

    builder = DatasetBuilder(
        dataset_dir=args.dataset_dir,
        chunk_size=args.chunk_size,
        chunk_overlap=args.overlap,
        web_include_dirs=args.web_include_dirs,
        web_exclude_dirs=args.web_exclude_dirs,
        clean_text=not args.no_clean,
        clean_aggressive=args.clean_aggressive,
        clean_min_line_length=args.clean_min_line_length,
    )

    if args.stats:
        builder.stats()
        return

    builder.build(incremental=args.incremental, clear_existing=args.clear)
    builder.stats()


if __name__ == "__main__":
    main()

