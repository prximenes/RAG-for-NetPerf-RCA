---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/get-started/docker-concepts/building-images/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.584089+00:00"
}
                    ---
                    # content/get-started/docker-concepts/building-images/_index.md

                    ---
title: Building images
weight: 20
keywords: build images, Dockerfile, layers, tag, push, cache, multi-stage
description: |
  Learn how to build Docker images from a Dockerfile. You'll understand the
  structure of a Dockerfile, how to build an image, and how to customize the
  build process.
summary: |
  Building container images is both technical and an art. You want to keep the
  image small and focused to increase your security posture, but also need to
  balance potential tradeoffs, such as caching impacts. In this series, you’ll
  deep dive into the secrets of images, how they are built and best practices.
layout: series
params:
  skill: Beginner
  time: 25 minutes
  prereq: None
---

## About this series

Learn how to build production-ready images that are lean and efficient Docker
images, essential for minimizing overhead and enhancing deployment in
production environments.

## What you'll learn

- Understanding image layers
- Writing a Dockerfile
- Build, tag and publish an image
- Using the build cache
- Multi-stage builds
