---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/guides/docker-build-cloud/ci.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.807643+00:00"
}
                    ---
                    # content/guides/docker-build-cloud/ci.md

                    ---
title: "Demo: Using Docker Build Cloud in CI"
description: Learn how to use Docker Build Cloud to build your app faster in CI.
weight: 30
---

Docker Build Cloud can significantly decrease the time it takes for your CI builds
take to run, saving you time and money. 

Since the builds run remotely, your CI runner can still use the Docker tooling CLI
without needing elevated permissions, making your builds more secure by default.

In this demo, you will see:

- How to integrate Docker Build Cloud into a variety of CI platforms
- How to use Docker Build Cloud in GitHub Actions to build multi-architecture images
- Speed differences between a workflow using Docker Build Cloud and a workflow running natively
- How to use Docker Build Cloud in a GitLab Pipeline

{{< youtube-embed "wvLdInoVBGg" >}}

<div id="dbc-lp-survey-anchor"></div>
