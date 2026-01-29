---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/reference/api/extensions-sdk/ServiceError.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.747799+00:00"
}
                    ---
                    # content/reference/api/extensions-sdk/ServiceError.md

                    ---
title: "Interface: ServiceError"
description: Docker extension API reference
keywords: Docker, extensions, sdk, API, reference
aliases:
 - /desktop/extensions-sdk/dev/api/reference/interfaces/ServiceError/
 - /extensions/extensions-sdk/dev/api/reference/interfaces/ServiceError/
---

Error thrown when an HTTP response is received with a status code that falls
out to the range of 2xx.

**`Since`**

0.2.0

## Properties

### name

• **name**: `string`

___

### message

• **message**: `string`

___

### statusCode

• **statusCode**: `number`
