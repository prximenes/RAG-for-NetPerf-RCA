---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/dhi/about/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:13.044217+00:00"
}
                    ---
                    # content/manuals/dhi/about/_index.md

                    ---
title: About
description: Learn about Docker Hardened Images, their purpose, how they are built and tested, and the shared responsibility model for security.
weight: 5
params:
  grid_about:
    - title: What are hardened images and why use them?
      description: Learn what a hardened image is, how Docker Hardened Images are built, what sets them apart from typical base and application images, and why you should use them.
      icon: info
      link: /dhi/about/what/
    - title: Build process
      description: Learn how Docker builds, tests, and maintains Docker Hardened Images through an automated, security-focused pipeline.
      icon: build
      link: /dhi/about/build-process/
    - title: Image testing
      description: See how Docker Hardened Images are automatically tested for standards compliance, functionality, and security.
      icon: science
      link: /dhi/about/test/
    - title: Responsibility overview
      description: Understand Docker's role and your responsibilities when using Docker Hardened Images as part of your secure software supply chain.
      icon: group
      link: /dhi/about/responsibility/
    - title: Image types
      description: Learn about the different image types, distributions, and variants offered in the Docker Hardened Images catalog.
      icon: view_module
      link: /dhi/about/available/
    - title: Questions, bugs, or feedback
      icon: question_exchange
      description: Docker welcomes all contributions and feedback — whether it’s a bug report, feature suggestion, or security concern.
      link: /dhi/about/feedback 
---

Docker Hardened Images (DHIs) are purpose-built for security, compliance, and
reliability in modern software supply chains. This section explains what makes
these images different from standard base and application images, how they're
built and tested, and how Docker and users share responsibility in securing
containerized workloads.

## Learn about Docker Hardened Images

{{< grid
  items="grid_about"
>}}
