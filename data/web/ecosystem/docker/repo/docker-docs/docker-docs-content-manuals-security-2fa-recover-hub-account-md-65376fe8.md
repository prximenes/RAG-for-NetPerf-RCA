---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/security/2fa/recover-hub-account.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:13.031931+00:00"
}
                    ---
                    # content/manuals/security/2fa/recover-hub-account.md

                    ---
title: Recover your Docker account
description: Recover your Docker account and manage two-factor authentication recovery codes
keywords: account recovery, two-factor authentication, 2FA, recovery code, docker hub security
aliases:
 - /docker-hub/2fa/recover-hub-account/
 - /security/for-developers/2fa/recover-hub-account/
 - /security/2fa/new-recovery-code/
weight: 20
---

This page explains how to recover your Docker account and manage recovery codes for two-factor authentication.

## Generate a new recovery code

If you lost your two-factor authentication recovery code but still have access to your Docker Hub account, you can generate a new recovery code.

1. Sign in to your [Docker account](https://app.docker.com/login) with your username and password.
1. Select your avatar and from the drop-down menu, select **Account settings**.
1. Select **2FA**.
1. Enter your password, then select **Confirm**.
1. Select **Generate new code**.

This generates a new code. Select the visibility icon to view the code. Save your recovery code and store it somewhere safe.

## Recover your account without access

If you lost access to both your two-factor authentication application and your recovery code:

1. Sign in to your [Docker account](https://app.docker.com/login) with your username and password.
1. Select **I've lost my authentication device** and **I've lost my recovery code**.
1. Complete the [Contact Support form](https://hub.docker.com/support/contact/?category=2fa-lockout).

You must enter the primary email address associated with your Docker ID in the Contact Support form for recovery instructions.
