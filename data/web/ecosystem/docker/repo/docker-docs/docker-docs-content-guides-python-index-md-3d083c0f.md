---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/guides/python/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.830245+00:00"
}
                    ---
                    # content/guides/python/_index.md

                    ---
title: Python language-specific guide
linkTitle: Python
description: Containerize Python apps using Docker
keywords: Docker, getting started, Python, language
summary: |
  This guide explains how to containerize Python applications using Docker.
toc_min: 1
toc_max: 2
aliases:
  - /language/python/
  - /guides/language/python/
languages: [python]
params:
  time: 20 minutes
---

> **Acknowledgment**
>
> This guide is a community contribution. Docker would like to thank
> [Esteban Maya](https://www.linkedin.com/in/esteban-x64/) and [Igor Aleksandrov](https://www.linkedin.com/in/igor-aleksandrov/) for their contribution
> to this guide.

The Python language-specific guide teaches you how to containerize a Python application using Docker. In this guide, you’ll learn how to:

- Containerize and run a Python application
- Set up a local environment to develop a Python application using containers
- Lint, format, typing and best practices
- Configure a CI/CD pipeline for a containerized Python application using GitHub Actions
- Deploy your containerized Python application locally to Kubernetes to test and debug your deployment

Start by containerizing an existing Python application.
