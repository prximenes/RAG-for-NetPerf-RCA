---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/build/cache/backends/azblob.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:13.087773+00:00"
}
                    ---
                    # content/manuals/build/cache/backends/azblob.md

                    ---
title: Azure Blob Storage cache
description: Manage build cache with Azure blob storage
keywords: build, buildx, cache, backend, azblob, azure
aliases:
  - /build/building/cache/backends/azblob/
---

{{< summary-bar feature_name="Azure blob" >}}

The `azblob` cache store uploads your resulting build cache to
[Azure's blob storage service](https://azure.microsoft.com/en-us/services/storage/blobs/).

This cache storage backend is not supported with the default `docker` driver.
To use this feature, create a new builder using a different driver. See
[Build drivers](/manuals/build/builders/drivers/_index.md) for more information.

## Synopsis

```console
$ docker buildx build --push -t <registry>/<image> \
  --cache-to type=azblob,name=<cache-image>[,parameters...] \
  --cache-from type=azblob,name=<cache-image>[,parameters...] .
```

The following table describes the available CSV parameters that you can pass to
`--cache-to` and `--cache-from`.

| Name                | Option                  | Type        | Default | Description                                        |
| ------------------- | ----------------------- | ----------- | ------- | -------------------------------------------------- |
| `name`              | `cache-to`,`cache-from` | String      |         | Required. The name of the cache image.             |
| `account_url`       | `cache-to`,`cache-from` | String      |         | Base URL of the storage account.                   |
| `secret_access_key` | `cache-to`,`cache-from` | String      |         | Blob storage account key, see [authentication][1]. |
| `mode`              | `cache-to`              | `min`,`max` | `min`   | Cache layers to export, see [cache mode][2].       |
| `ignore-error`      | `cache-to`              | Boolean     | `false` | Ignore errors caused by failed cache exports.      |

[1]: #authentication
[2]: _index.md#cache-mode

## Authentication

The `secret_access_key`, if left unspecified, is read from environment variables
on the BuildKit server following the scheme for the
[Azure Go SDK](https://docs.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication).
The environment variables are read from the server, not the Buildx client.

## Further reading

For an introduction to caching see [Docker build cache](../_index.md).

For more information on the `azblob` cache backend, see the
[BuildKit README](https://github.com/moby/buildkit#azure-blob-storage-cache-experimental).
