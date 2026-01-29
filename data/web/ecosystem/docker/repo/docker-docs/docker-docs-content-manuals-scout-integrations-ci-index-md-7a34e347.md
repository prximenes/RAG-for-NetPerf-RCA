---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/scout/integrations/ci/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:13.131988+00:00"
}
                    ---
                    # content/manuals/scout/integrations/ci/_index.md

                    ---
description: How to setup Docker Scout in continuous integration pipelines
keywords: scanning, vulnerabilities, Hub, supply chain, security, ci, continuous integration,
  github actions, gitlab
title: Using Docker Scout in continuous integration
linkTitle: Continuous Integration
aliases:
- /scout/ci/
---

You can analyze Docker images in continuous integration pipelines as you build
them using a GitHub action or the Docker Scout CLI plugin.

Available integrations:

- [GitHub Actions](gha.md)
- [GitLab](gitlab.md)
- [Microsoft Azure DevOps Pipelines](azure.md)
- [Circle CI](circle-ci.md)
- [Jenkins](jenkins.md)

You can also add runtime integration as part of your CI/CD pipeline, which lets
you assign an image to an environment, such as `production` or `staging`, when
you deploy it. For more information, see [Environment monitoring](../environment/_index.md).
