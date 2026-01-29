---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/guides/rag-ollama/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.790461+00:00"
}
                    ---
                    # content/guides/rag-ollama/_index.md

                    ---
description: Containerize RAG application using Ollama and Docker
keywords: python, generative ai, genai, llm, ollama, rag, qdrant
title: Build a RAG application using Ollama and Docker
linkTitle: RAG Ollama application
summary: |
  This guide demonstrates how to use Docker to deploy Retrieval-Augmented
  Generation (RAG) models with Ollama.
tags: [ai]
aliases:
  - /guides/use-case/rag-ollama/
params:
  time: 20 minutes
---

The Retrieval Augmented Generation (RAG) guide teaches you how to containerize an existing RAG application using Docker. The example application is a RAG that acts like a sommelier, giving you the best pairings between wines and food. In this guide, you’ll learn how to:

- Containerize and run a RAG application
- Set up a local environment to run the complete RAG stack locally for development

Start by containerizing an existing RAG application.
