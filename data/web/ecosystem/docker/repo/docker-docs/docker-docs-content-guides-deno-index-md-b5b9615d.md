---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/guides/deno/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.773773+00:00"
}
                    ---
                    # content/guides/deno/_index.md

                    ---
description: Containerize and develop Deno applications using Docker.
keywords: getting started, deno
title: Deno language-specific guide
summary: |
  Learn how to containerize JavaScript applications with the Deno runtime using Docker.
linkTitle: Deno
languages: [js]
params:
  time: 10 minutes
---

The Deno getting started guide teaches you how to create a containerized Deno application using Docker.

> **Acknowledgment**
>
> Docker would like to thank [Pradumna Saraf](https://twitter.com/pradumna_saraf) for his contribution to this guide.

## What will you learn?

* Containerize and run a Deno application using Docker
* Set up a local environment to develop a Deno application using containers
* Use Docker Compose to run the application.
* Configure a CI/CD pipeline for a containerized Deno application using GitHub Actions
* Deploy your containerized application locally to Kubernetes to test and debug your deployment

## Prerequisites

- Basic understanding of JavaScript is assumed.
- You must have familiarity with Docker concepts like containers, images, and Dockerfiles. If you are new to Docker, you can start with the [Docker basics](/get-started/docker-concepts/the-basics/what-is-a-container.md) guide.

After completing the Deno getting started modules, you should be able to containerize your own Deno application based on the examples and instructions provided in this guide.

Start by containerizing an existing Deno application.
