---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/guides/docker-scout/remediation.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.823009+00:00"
}
                    ---
                    # content/guides/docker-scout/remediation.md

                    ---
title: Remediation
description: Learn how Docker Scout can help you improve your software quality automatically, using remediation
keywords: scout, supply chain, security, remediation, automation
weight: 60
---

{{< youtube-embed jM9zLBf8M-8 >}}

Docker Scout's [remediation feature](/manuals/scout/policy/remediation.md)
helps you address supply chain and security issues by offering tailored
recommendations based on policy evaluations. These recommendations guide you in
improving policy compliance or enhancing image metadata, allowing Docker Scout
to perform more accurate evaluations in the future.

You can use this feature to ensure that your base images are up-to-date and
that your supply chain attestations are complete. When a violation occurs,
Docker Scout provides recommended fixes, such as updating your base image or
adding missing attestations. If there isn’t enough information to determine
compliance, Docker Scout suggests actions to help resolve the issue.

In the Docker Scout Dashboard, you can view and act on these recommendations by
reviewing violations or compliance uncertainties. With integrations like
GitHub, you can even automate updates, directly fixing issues from the
dashboard.

<div id="scout-lp-survey-anchor"></div>
