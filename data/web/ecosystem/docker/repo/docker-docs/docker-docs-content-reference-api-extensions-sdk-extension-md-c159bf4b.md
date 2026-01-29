---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/reference/api/extensions-sdk/Extension.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.742208+00:00"
}
                    ---
                    # content/reference/api/extensions-sdk/Extension.md

                    ---
title: "Interface: Extension"
description: Docker extension API reference
keywords: Docker, extensions, sdk, API, reference
aliases:
 - /desktop/extensions-sdk/dev/api/reference/interfaces/Extension/
 - /extensions/extensions-sdk/dev/api/reference/interfaces/Extension/
---

**`Since`**

0.2.0

## Properties

### vm

• `Optional` `Readonly` **vm**: [`ExtensionVM`](ExtensionVM.md)

___

### host

• `Optional` `Readonly` **host**: [`ExtensionHost`](ExtensionHost.md)

___

### image

• `Readonly` **image**: `string`

**`Since`**

0.3.3
