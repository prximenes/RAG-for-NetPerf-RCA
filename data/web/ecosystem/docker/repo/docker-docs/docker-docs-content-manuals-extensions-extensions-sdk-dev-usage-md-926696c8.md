---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/extensions/extensions-sdk/dev/usage.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.907615+00:00"
}
                    ---
                    # content/manuals/extensions/extensions-sdk/dev/usage.md

                    ---
title: CLI reference
description: Docker extension CLI
keywords: Docker, extensions, sdk, CLI
aliases:
 - /desktop/extensions-sdk/dev/cli/usage/
 - /desktop/extensions-sdk/dev/usage/
weight: 30
---

The Extensions CLI is an extension development tool that is used to manage Docker extensions. Actions include install, list, remove, and validate extensions.

- `docker extension enable` turns on Docker extensions.
- `docker extension dev` commands for extension development.
- `docker extension disable` turns off Docker extensions.
- `docker extension init` creates a new Docker extension.
- `docker extension install` installs a Docker extension with the specified image.
- `docker extension ls` list installed Docker extensions.
- `docker extension rm` removes a Docker extension.
- `docker extension update` removes and re-installs a Docker extension.
- `docker extension validate` validates the extension metadata file against the JSON schema.
