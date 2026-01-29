---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/build/ci/github-actions/manage-tags-labels.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:13.091261+00:00"
}
                    ---
                    # content/manuals/build/ci/github-actions/manage-tags-labels.md

                    ---
title: Manage tags and labels with GitHub Actions
linkTitle: Tags and labels
description: Assign tags and labels to images automatically with GitHub Actions
keywords: ci, github actions, gha, buildkit, buildx, tags, labels
---

If you want an "automatic" tag management and [OCI Image Format Specification](https://github.com/opencontainers/image-spec/blob/master/annotations.md)
for labels, you can do it in a dedicated setup step. The following workflow
will use the [Docker Metadata Action](https://github.com/docker/metadata-action)
to handle tags and labels based on GitHub Actions events and Git metadata:

```yaml
name: ci

on:
  schedule:
    - cron: "0 10 * * *"
  push:
    branches:
      - "**"
    tags:
      - "v*.*.*"
  pull_request:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Docker meta
        id: meta
        uses: docker/metadata-action@v5
        with:
          # list of Docker images to use as base name for tags
          images: |
            name/app
            ghcr.io/username/app
          # generate Docker tags based on the following events/attributes
          tags: |
            type=schedule
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=semver,pattern={{major}}
            type=sha

      - name: Login to Docker Hub
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v3
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Login to GHCR
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.repository_owner }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Set up QEMU
        uses: docker/setup-qemu-action@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build and push
        uses: docker/build-push-action@v6
        with:
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
```
