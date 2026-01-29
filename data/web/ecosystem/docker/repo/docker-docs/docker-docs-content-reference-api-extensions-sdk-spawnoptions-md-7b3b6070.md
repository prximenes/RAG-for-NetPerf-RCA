---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/reference/api/extensions-sdk/SpawnOptions.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.741157+00:00"
}
                    ---
                    # content/reference/api/extensions-sdk/SpawnOptions.md

                    ---
title: "Interface: SpawnOptions"
description: Docker extension API reference
keywords: Docker, extensions, sdk, API, reference
aliases:
 - /desktop/extensions-sdk/dev/api/reference/interfaces/SpawnOptions/
 - /extensions/extensions-sdk/dev/api/reference/interfaces/SpawnOptions/
---

**`Since`**

0.3.0

## Hierarchy

- [`ExecOptions`](ExecOptions.md)

  ↳ **`SpawnOptions`**

## Properties

### cwd

• `Optional` **cwd**: `string`

#### Inherited from

[ExecOptions](ExecOptions.md).[cwd](ExecOptions.md#cwd)

___

### env

• `Optional` **env**: `ProcessEnv`

#### Inherited from

[ExecOptions](ExecOptions.md).[env](ExecOptions.md#env)

___

### stream

• **stream**: [`ExecStreamOptions`](ExecStreamOptions.md)
