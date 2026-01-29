---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/compose/how-tos/environment-variables/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:13.115040+00:00"
}
                    ---
                    # content/manuals/compose/how-tos/environment-variables/_index.md

                    ---
title: Environment variables in Compose
linkTitle: Use environment variables
weight: 40
description: Explains how to set, use, and manage environment variables in Docker Compose.
keywords: compose, orchestration, environment, env file
aliases:
- /compose/environment-variables/
---

Environment variables and interpolation in Docker Compose help you create reusable, flexible configurations. This makes Dockerized applications easier to manage and deploy across environments.

> [!TIP]
>
> Before using environment variables, read through all of the information first to get a full picture of environment variables in Docker Compose.

This section covers:

- [How to set environment variables within your container's environment](set-environment-variables.md).
- [How environment variable precedence works within your container's environment](envvars-precedence.md).
- [Pre-defined environment variables](envvars.md).

It also covers: 
- How [interpolation](variable-interpolation.md) can be used to set variables within your Compose file and how it relates to a container's environment.
- Some [best practices](best-practices.md).
