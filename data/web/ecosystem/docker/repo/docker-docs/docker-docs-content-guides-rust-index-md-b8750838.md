---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/guides/rust/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.827013+00:00"
}
                    ---
                    # content/guides/rust/_index.md

                    ---
title: Rust language-specific guide
linkTitle: Rust
description: Containerize Rust apps using Docker
keywords: Docker, getting started, Rust, language
summary: |
  This guide covers how to containerize Rust applications using Docker.
toc_min: 1
toc_max: 2
aliases:
  - /language/rust/
  - /guides/language/rust/
languages: [rust]
params:
  time: 20 minutes
---

The Rust language-specific guide teaches you how to create a containerized Rust application using Docker. In this guide, you'll learn how to:

- Containerize a Rust application
- Build an image and run the newly built image as a container
- Set up volumes and networking
- Orchestrate containers using Compose
- Use containers for development
- Configure a CI/CD pipeline for your application using GitHub Actions
- Deploy your containerized Rust application locally to Kubernetes to test and debug your deployment

After completing the Rust modules, you should be able to containerize your own Rust application based on the examples and instructions provided in this guide.

Start with building your first Rust image.
