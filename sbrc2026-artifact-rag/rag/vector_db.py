import os
from pathlib import Path

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from rag.data_loader import EMBED_DIM


class QdrantStorage:
    def __init__(self, path: str | None = None, collection: str = "docs", dim: int = EMBED_DIM):
        if path is None:
            env_path = os.getenv("QDRANT_PATH")
            if env_path:
                path = env_path
            else:
                # Default: store alongside this artifact repo (./qdrant_storage)
                default_path = Path(__file__).resolve().parent.parent / "qdrant_storage"
                path = str(default_path)

        self.client = QdrantClient(path=path)
        self.collection = collection

        if not self.client.collection_exists(self.collection):
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
            )

    def upsert(self, ids, vectors, payloads):
        points = [PointStruct(id=ids[i], vector=vectors[i], payload=payloads[i]) for i in range(len(ids))]
        self.client.upsert(self.collection, points=points)

    def search(self, query_vector, top_k: int = 5):
        # qdrant-client==1.15.1 supports `.search`
        results = self.client.search(
            collection_name=self.collection,
            query_vector=query_vector,
            with_payload=True,
            limit=top_k,
        )
        contexts = []
        sources = set()

        for r in results:
            payload = getattr(r, "payload", None) or {}
            text = payload.get("text", "")
            source = payload.get("source", "")
            if text:
                contexts.append(text)
                sources.add(source)

        return {"contexts": contexts, "sources": list(sources)}

    def clear_collection(self):
        if self.client.collection_exists(self.collection):
            self.client.delete_collection(self.collection)

        self.client.create_collection(
            collection_name=self.collection,
            vectors_config=VectorParams(size=EMBED_DIM, distance=Distance.COSINE),
        )

    def dataset_exists(self) -> bool:
        if not self.client.collection_exists(self.collection):
            return False
        collection_info = self.client.get_collection(self.collection)
        return collection_info.points_count > 0

