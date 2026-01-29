---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/dhi/features/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:13.034542+00:00"
}
                    ---
                    # content/manuals/dhi/features/_index.md

                    ---
title: Features
description: Explore the core features of Docker Hardened Images, including hardened defaults, secure metadata, and ecosystem compatibility.
weight: 10
params:
  grid_features:
    - title: Hardened, secure images
      description: Learn how Docker Hardened Images reduce vulnerabilities, enforce non-root execution, and include SLSA-compliant metadata for supply chain security.
      icon: lock
      link: /dhi/features/secure/
    - title: Seamless integration
      description: See how Docker Hardened Images integrate with CI/CD pipelines, vulnerability scanners, and container registries across your toolchain.
      icon: hub
      link: /dhi/features/integration/
    - title: Enterprise support
      description: Learn about enterprise support and SLA-driven updates.
      icon: settings
      link: /dhi/features/support/
    - title: Continuous patching and secure maintenance
      description: Learn how Docker Hardened Images are continuously updated with security patches, ensuring your images remain secure over time.
      icon: dashboard
      link: /dhi/features/patching/
    - title: Flexible, repository-based pricing
      description: Learn how Docker Hardened Images offer repository-based flexibility with no per-image or per-pull limitations.
      icon: wallet
      link: /dhi/features/flexible/
    - title: Docker Hardened Image charts
      description: Learn about Docker Hardened Image charts.
      icon: leaderboard
      link: /dhi/features/helm/
---

Docker Hardened Images (DHIs) go beyond minimal base and application images by
incorporating hardened defaults, signed metadata, and broad ecosystem
compatibility. Whether you're securing a single service or rolling out
compliance controls at scale, this section covers the key features that make
DHIs production-ready.

## Explore core features

{{< grid
  items="grid_features"
>}}
