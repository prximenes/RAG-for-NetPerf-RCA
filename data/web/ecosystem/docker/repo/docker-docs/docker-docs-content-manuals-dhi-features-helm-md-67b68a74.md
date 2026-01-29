---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/dhi/features/helm.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:13.035362+00:00"
}
                    ---
                    # content/manuals/dhi/features/helm.md

                    ---
title: Docker Hardened Image charts
linktitle: Helm charts
description: Learn about Docker Hardened Image charts.
keywords: docker hardened images helm, dhi helm charts, kubernetes hardened images, k8s hardened images
---

Docker Hardened Image (DHI) charts are Docker-provided Helm charts built from upstream and community-maintained sources,
designed for compatibility with Docker Hardened Images. These charts are available as OCI artifacts within the DHI
catalog on Docker Hub.

## Comprehensive supply chain security

Like the hardened images, DHI charts incorporate multiple layers of security metadata to ensure transparency and trust:

- SLSA Level 3 compliance: Each chart is built with Docker's SLSA Build Level 3 system, including a detailed build
  provenance, and meeting the standards set by the Supply-chain Levels for Software Artifacts (SLSA) framework.
- Software Bill of Materials (SBOMs): Comprehensive SBOMs are provided, detailing all components referenced within the
  chart to facilitate vulnerability management and compliance audits.
- Cryptographic signing: All associated metadata is cryptographically signed by Docker, ensuring integrity and
  authenticity.
- Hardened configuration: Charts automatically reference Docker hardened images, ensuring security in deployments.

## Developer Friendly

DHI charts are robustly tested after building to ensure they work out-of-the-box with Docker Hardened Images. This
removes friction in migration and reduces developer workload in implementing the charts, ensuring seamless
compatibility.
