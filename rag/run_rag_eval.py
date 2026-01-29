#!/usr/bin/env python3
"""
Execução e avaliação em lote (RAG) usando:
- retrieval: Qdrant embedded (./qdrant_storage)
- generator: llama.cpp `llama-server` (OpenAI-compatible endpoint)
- cenários: JSONL em ./scenarios/prompts.jsonl
- gabaritos: JSONL em ./scenarios/answers.jsonl

Saída: arquivos JSON por (scenario_id, resposta_id) + run_meta.json
"""

import argparse
import json
import os
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from openai import OpenAI

from rag.data_loader import embed_texts
from rag.vector_db import QdrantStorage


@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    scenario_name: str
    prompt: str
    expected: dict[str, Any] | None


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        items.append(json.loads(line))
    return items


def load_scenarios(prompts_jsonl: Path, answers_jsonl: Path) -> list[Scenario]:
    prompts = _read_jsonl(prompts_jsonl)
    answers = _read_jsonl(answers_jsonl)

    by_id: dict[str, dict[str, Any]] = {a["scenario_id"]: a for a in answers if "scenario_id" in a}

    out: list[Scenario] = []
    for p in prompts:
        sid = p["scenario_id"]
        ans = by_id.get(sid)
        expected = None
        if ans is not None:
            expected = {
                "diagnosis": ans.get("diagnosis"),
                "confidence": ans.get("confidence"),
                "evidence": ans.get("evidence"),
                "next_steps": ans.get("next_steps"),
            }
        out.append(
            Scenario(
                scenario_id=sid,
                scenario_name=p.get("scenario_name", sid),
                prompt=p["prompt"],
                expected=expected,
            )
        )
    return out


def build_rag_prompt(prompt: str, contexts: list[str], sources: list[str], max_ctx_chars: int, max_ctx_per_chunk: int) -> str:
    clipped: list[str] = []
    remaining = max_ctx_chars
    for c in contexts:
        if remaining <= 0:
            break
        c = (c or "").strip()
        if not c:
            continue
        c = c[: min(max_ctx_per_chunk, remaining)]
        clipped.append(c)
        remaining -= len(c)

    ctx_block = "\n\n".join(f"[chunk {i+1}] {c}" for i, c in enumerate(clipped)) if clipped else "(none)"
    src_block = "\n".join(f"- {s}" for s in sources) if sources else "(none)"

    return (
        f"{prompt}\n\n"
        "=== Retrieved Knowledge Base (RAG) ===\n"
        "Use this ONLY if it helps; otherwise prefer the Collected Data inside the prompt.\n\n"
        f"SOURCES:\n{src_block}\n\n"
        f"CONTEXT:\n{ctx_block}\n"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/run", help="Diretório de saída")
    ap.add_argument("--limit", type=int, default=0, help="Limita número de cenários (0 = todos)")
    ap.add_argument("--responses-per-scenario", type=int, default=3)
    ap.add_argument("--llamacpp-url", default="http://localhost:8080")
    ap.add_argument("--model", default=os.getenv("LLM_MODEL", "unknown"), help="Nome do modelo (apenas para log)")
    ap.add_argument("--top-k", type=int, default=int(os.getenv("RAG_TOP_K", "5")))
    ap.add_argument("--max-ctx-chars", type=int, default=int(os.getenv("RAG_MAX_CTX_CHARS", "8000")))
    ap.add_argument("--max-ctx-per-chunk", type=int, default=int(os.getenv("RAG_MAX_CTX_PER_CHUNK", "1200")))
    args = ap.parse_args()

    repo_dir = Path(__file__).resolve().parent.parent
    prompts_jsonl = repo_dir / "scenarios" / "prompts.jsonl"
    answers_jsonl = repo_dir / "scenarios" / "answers.jsonl"

    scenarios = load_scenarios(prompts_jsonl, answers_jsonl)
    if args.limit and args.limit > 0:
        scenarios = scenarios[: args.limit]

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    store = QdrantStorage(path=str(repo_dir / "qdrant_storage"))
    client = OpenAI(base_url=f"{args.llamacpp_url}/v1", api_key="not-needed")

    run_meta = {
        "timestamp": datetime.now().isoformat(),
        "llamacpp_url": args.llamacpp_url,
        "model": args.model,
        "top_k": args.top_k,
        "max_ctx_chars": args.max_ctx_chars,
        "max_ctx_per_chunk": args.max_ctx_per_chunk,
        "responses_per_scenario": args.responses_per_scenario,
        "num_scenarios": len(scenarios),
    }
    (out_dir / "run_meta.json").write_text(json.dumps(run_meta, indent=2), encoding="utf-8")

    for idx, sc in enumerate(scenarios, 1):
        print(f"[{idx}/{len(scenarios)}] {sc.scenario_id} ({sc.scenario_name})")

        try:
            qvec = embed_texts([sc.prompt])[0]
            found = store.search(qvec, top_k=args.top_k)
            contexts = found.get("contexts") or []
            sources = found.get("sources") or []
        except Exception as e:
            print(f"  retrieval error: {e}")
            contexts, sources = [], []

        rag_prompt = build_rag_prompt(
            sc.prompt, contexts, sources, max_ctx_chars=args.max_ctx_chars, max_ctx_per_chunk=args.max_ctx_per_chunk
        )

        for rid in range(1, args.responses_per_scenario + 1):
            t0 = time.time()
            resp = client.chat.completions.create(
                model=args.model,
                messages=[{"role": "user", "content": rag_prompt}],
                temperature=0.7,
                max_tokens=2048,
                stream=False,
            )
            dt = time.time() - t0

            content = getattr(resp.choices[0].message, "content", None)
            usage = getattr(resp, "usage", None)
            usage_info = None
            if usage is not None:
                usage_info = {
                    "prompt_tokens": getattr(usage, "prompt_tokens", None),
                    "completion_tokens": getattr(usage, "completion_tokens", None),
                    "total_tokens": getattr(usage, "total_tokens", None),
                }

            result = {
                "scenario_id": sc.scenario_id,
                "scenario_name": sc.scenario_name,
                "resposta_id": rid,
                "engine": "llama-cpp-openai-rag",
                "model": args.model,
                "prompt": sc.prompt,
                "rag": {
                    "top_k": args.top_k,
                    "sources": sources,
                    "contexts_preview": [(c or "")[: args.max_ctx_per_chunk] for c in contexts[: args.top_k]],
                },
                "response": content,
                "expected": sc.expected,
                "latency_s": dt,
                "usage": usage_info,
                "timestamp": datetime.now().isoformat(),
            }

            out_path = out_dir / f"{sc.scenario_id}_resposta_{rid}.json"
            out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()

