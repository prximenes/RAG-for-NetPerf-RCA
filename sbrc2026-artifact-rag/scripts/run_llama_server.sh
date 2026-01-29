#!/usr/bin/env bash
set -euo pipefail

# Ajuste UM destes:
# - Para GGUF local:
#   MODEL_PATH="/caminho/para/modelo.gguf"
#   EXTRA_ARGS=(-m "$MODEL_PATH")
#
# - Para Hugging Face (requer suporte -hf no seu llama-server):
#   HF_MODEL_ID="unsloth/gemma-3-12b-it-GGUF:Q4_K_M"
#   EXTRA_ARGS=(-hf "$HF_MODEL_ID")
#
# IMPORTANTE: não comite tokens. Se precisar:
#   export HF_TOKEN="..."

HOST="${HOST:-127.0.0.1}"
PORT="${PORT:-8080}"
CTX_SIZE="${CTX_SIZE:-16384}"
N_GPU_LAYERS="${N_GPU_LAYERS:-999}"

# Default: HF model id (mais simples para avaliadores). Troque se quiser GGUF local.
HF_MODEL_ID="${HF_MODEL_ID:-unsloth/gemma-3-12b-it-GGUF:Q4_K_M}"

EXTRA_ARGS=(-hf "$HF_MODEL_ID")

echo "Starting llama-server"
echo "  model: ${HF_MODEL_ID}"
echo "  url:   http://${HOST}:${PORT}"

exec llama-server \
  "${EXTRA_ARGS[@]}" \
  --host "$HOST" \
  --port "$PORT" \
  --ctx-size "$CTX_SIZE" \
  --n-gpu-layers "$N_GPU_LAYERS" \
  --verbose

