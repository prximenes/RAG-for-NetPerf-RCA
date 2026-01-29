---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/guides/docker-compose/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.771943+00:00"
}
                    ---
                    # content/guides/docker-compose/_index.md

                    ---
title: Defining and running multi-container applications with Docker Compose
linkTitle: Docker Compose
summary: |
  Simplify the process of defining, configuring, and running multi-container
  Docker applications.
description: Learn how to use Docker Compose to define and run multi-container Docker applications.
tags: [product-demo]
aliases:
  - /learning-paths/docker-compose/
params:
  image: images/learning-paths/compose.png
  time: 10 minutes
  resource_links:
    - title: Overview of Docker Compose CLI
      url: /compose/reference/
    - title: Overview of Docker Compose
      url: /compose/
    - title: How Compose works
      url: /compose/intro/compose-application-model/
    - title: Using profiles with Compose
      url: /compose/how-tos/profiles/
    - title: Control startup and shutdown order with Compose
      url: /compose/how-tos/startup-order/
    - title: Compose Build Specification
      url: /compose/compose-file/build/
---

Developers face challenges with multi-container Docker applications, including
complex configuration, dependency management, and maintaining consistent
environments. Networking, resource allocation, data persistence, logging, and
monitoring add to the difficulty. Security concerns and troubleshooting issues
further complicate the process, requiring effective tools and practices for
efficient management.

Docker Compose solves the problem of managing multi-container Docker
applications by providing a simple way to define, configure, and run all the
containers needed for an application using a single YAML file. This approach
helps developers to easily set up, share, and maintain consistent development,
testing, and production environments, ensuring that complex applications can be
deployed with all their dependencies and services properly configured and
orchestrated.

## What you’ll learn

- What Docker Compose is and what it does
- How to define services
- Use cases for Docker Compose
- How things would be different without Docker Compose

## Who’s this for?

- Developers and DevOps engineers who need to define, manage, and orchestrate
  multi-container Docker applications efficiently across multiple environments.
- Development teams that want to increase productivity by streamlining
  development workflows and reducing setup time.

## Tools integration

Works well with Docker CLI, CI/CD tools, and container orchestration tools.

<div id="compose-lp-survey-anchor"></div>
