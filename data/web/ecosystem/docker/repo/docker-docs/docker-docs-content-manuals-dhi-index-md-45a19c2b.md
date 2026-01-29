---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/dhi/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.847265+00:00"
}
                    ---
                    # content/manuals/dhi/_index.md

                    ---
title: Docker Hardened Images
description: Secure, minimal, and production-ready base images
weight: 13
params:
  sidebar:
    badge:
      color: green
      text: New
    group: Products
  grid_sections:
    - title: Quickstart
      description: Follow a step-by-step guide to explore, mirror, and run a Docker Hardened Image.
      icon: rocket_launch
      link: /dhi/get-started/
    - title: About
      description: Learn what Docker Hardened Images are, how they're built, and what sets them apart from typical base images.
      icon: info
      link: /dhi/about/
    - title: Features
      description: Discover the security, compliance, and enterprise-readiness features built into Docker Hardened Images.
      icon: lock
      link: /dhi/features/
    - title: How-tos
      description: Step-by-step guides for using, verifying, scanning, and migrating to Docker Hardened Images.
      icon: play_arrow
      link: /dhi/how-to/
    - title: Core concepts
      description: Understand the secure supply chain principles that make Docker Hardened Images production-ready.
      icon: fact_check
      link: /dhi/core-concepts/
    - title: Troubleshoot
      description: Resolve common issues with building, running, or debugging Docker Hardened Images.
      icon: help_center
      link: /dhi/troubleshoot/
---

{{< summary-bar feature_name="Docker Hardened Images" >}}

Docker Hardened Images (DHIs) are minimal, secure, and production-ready
container base and application images maintained by Docker. Designed to reduce
vulnerabilities and simplify compliance, DHIs integrate easily into your
existing Docker-based workflows with little to no retooling required.

Explore the sections below to get started with Docker Hardened Images, integrate
them into your workflow, and learn what makes them secure and enterprise-ready.

{{< grid
  items="grid_sections"
>}}
