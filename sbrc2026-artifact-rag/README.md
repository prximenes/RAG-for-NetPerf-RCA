# Título do Projeto

**Artefato SBRC 2026 — RAG para Diagnóstico de Cenários de Rede (RCA)**

Este repositório contém um artefato mínimo e autocontido para **executar um pipeline de Retrieval-Augmented Generation (RAG)** aplicado a diagnóstico/Root Cause Analysis (RCA) em cenários de redes/sistemas. O artefato inclui:

- **Base de conhecimento (KB)** em texto (amostra pequena) para indexação
- **Builder** para gerar embeddings e persistir um **Qdrant local (embedded)**
- **Execução do RAG**: retrieval no Qdrant + injeção de contexto no prompt + geração via `llama-server` (llama.cpp)
- **Avaliação** em lote com cenários (prompts) e gabaritos (answers) em JSONL

As instruções seguem o checklist de requisitos mínimos do SBRC 2026 (modelo em [Instruções de submissão - Avaliação de Artefato](https://doc-artefatos.github.io/sbrc2026/subinstrucoes.html)).

---

# Estrutura do README.md

Este `README.md` está organizado exatamente conforme o modelo exigido:

- **Selos Considerados**
- **Informações básicas**
- **Dependências**
- **Preocupações com segurança**
- **Instalação**
- **Teste mínimo**
- **Experimentos**
- **LICENSE**

---

# Selos Considerados

Os selos considerados são: **Disponíveis (SeloD)** e **Funcionais (SeloF)**.

> Observação: o pipeline é executável localmente e produz resultados reprodutíveis **condicionalmente** ao modelo gerador escolhido e ao ambiente (GPU/CPU). A seção “Experimentos” descreve um fluxo de reprodução.

---

# Informações básicas

## Objetivo do artefato

Demonstrar (i) como construímos o índice vetorial (Qdrant) a partir de documentação técnica, (ii) como executamos retrieval e injeção de contexto no prompt, e (iii) como executamos uma avaliação em lote em cenários de RCA.

## Ambiente de execução (referência)

- **OS**: Linux (Ubuntu/Debian-like recomendado)
- **Python**: 3.12+
- **CPU**: x86_64
- **GPU**: opcional (CUDA acelera embeddings e geração, mas não é obrigatório)
- **Disco**: ~5–20 GB dependendo do tamanho da KB (neste artefato, a KB é pequena)

---

# Dependências

## Dependências principais (Python)

Este artefato usa:

- `qdrant-client` (modo embedded/local)
- `transformers` + `torch` (embeddings com `Qwen/Qwen3-Embedding-0.6B`)
- `llama-index` (apenas para PDFs, se você adicionar PDFs)
- `openai` (cliente OpenAI compatível para falar com `llama-server` via endpoint OpenAI-style)

As dependências são instaladas via `uv` usando `pyproject.toml`.

## Dependências externas

- **llama.cpp** (necessário `llama-server`)
  - Guia oficial de build: `https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md`

---

# Preocupações com segurança

- **Chaves de API**:
  - Este repositório **não** inclui chaves.
  - Se você usar judge via API externa, guarde chaves em arquivos locais ignorados pelo Git (ex.: `.openrouter_key`).
- **Execução local**:
  - O `llama-server` abre uma porta HTTP. Execute em localhost ou rede confiável.
- **Conteúdo de dados**:
  - A KB incluída aqui é apenas uma amostra pequena. Ao adicionar mais dados, revise licenças e políticas do evento.

---

# Instalação

## 1) Clonar o repositório do artefato

```bash
git clone <URL_DO_REPO_DO_ARTEFATO>
cd sbrc2026-artifact-rag
```

## 2) Instalar `uv` (se necessário)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 3) Instalar dependências Python

```bash
uv sync
```

## 4) Instalar/compilar `llama-server` (llama.cpp)

Siga o guia oficial do llama.cpp:

- `https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md`

Após o build, garanta que `llama-server` está no seu `PATH` (ou ajuste o script em `scripts/run_llama_server.sh`).

---

# Teste mínimo

O teste mínimo executa:

1. build do índice vetorial (Qdrant embedded) a partir da KB de exemplo
2. start do `llama-server`
3. execução de uma avaliação curta (2 cenários) com RAG

## 1) Build do Qdrant (KB pequena)

```bash
uv run python rag/build_dataset.py --dataset-dir . --clear
```

Isso vai criar `./qdrant_storage/` (persistente) e imprimir estatísticas ao final.

## 2) Iniciar o `llama-server`

Em outro terminal:

```bash
bash scripts/run_llama_server.sh
```

## 3) Rodar a avaliação curta (2 cenários)

```bash
uv run python rag/run_rag_eval.py --limit 2 --out results/minimal_test
```

Ao final, você deve ver arquivos JSON em `results/minimal_test/`.

---

# Experimentos

## Experimento principal (avaliação em lote — 24 cenários)

### 1) Build do índice vetorial

```bash
uv run python rag/build_dataset.py --dataset-dir . --clear
```

> Para usar uma KB maior, substitua `kb_sample` por um diretório com seus dados (ex.: `data/web/...`) e ajuste `--web-include-dirs`/`--web-exclude-dirs`.

### 2) Iniciar o `llama-server`

```bash
bash scripts/run_llama_server.sh
```

### 3) Rodar avaliação completa com RAG

```bash
export RAG_TOP_K=5
uv run python rag/run_rag_eval.py --out results/full_eval
```

Saídas:

- `results/full_eval/run_meta.json` (metadados do run)
- `results/full_eval/<scenario_id>_resposta_<n>.json` (respostas e logs por cenário)

---

# LICENSE

Este artefato é distribuído sob a licença MIT. Veja o arquivo `LICENSE`.

