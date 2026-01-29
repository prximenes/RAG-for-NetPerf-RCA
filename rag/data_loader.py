from dotenv import load_dotenv
from transformers import AutoModel, AutoTokenizer
import torch
import torch.nn.functional as F

load_dotenv()

# Usando Qwen3-Embedding-0.6B para embeddings
print("🔄 Carregando Qwen3-Embedding-0.6B...")
embed_tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-Embedding-0.6B")
embed_model = AutoModel.from_pretrained(
    "Qwen/Qwen3-Embedding-0.6B",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto" if torch.cuda.is_available() else None,
)
embed_model.eval()

EMBED_DIM = 1024
print(f"✅ Modelo de embedding carregado! (Dimensão: {EMBED_DIM})")
print(f"   Dispositivo: {'GPU (CUDA)' if torch.cuda.is_available() else 'CPU'}")


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Gera embeddings usando Qwen3-Embedding-0.6B."""
    embeddings: list[list[float]] = []

    batch_size = 8
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]

        inputs = embed_tokenizer(
            batch,
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors="pt",
        )

        if torch.cuda.is_available():
            inputs = {k: v.to(embed_model.device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = embed_model(**inputs)
            attention_mask = inputs["attention_mask"]
            token_embeddings = outputs.last_hidden_state
            input_mask_expanded = (
                attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
            )
            sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
            sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
            batch_embeddings = sum_embeddings / sum_mask
            batch_embeddings = F.normalize(batch_embeddings, p=2, dim=1)
            embeddings.extend(batch_embeddings.cpu().float().tolist())

    return embeddings

