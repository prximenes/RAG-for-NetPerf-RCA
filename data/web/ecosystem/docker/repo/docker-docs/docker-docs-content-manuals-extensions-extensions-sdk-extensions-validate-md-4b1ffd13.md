---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/extensions/extensions-sdk/extensions/validate.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.904743+00:00"
}
                    ---
                    # content/manuals/extensions/extensions-sdk/extensions/validate.md

                    ---
title: Validate your extension
linkTitle: Validate
description: Step three in the extension creation process
keywords: Docker, Extensions, sdk, validate, install
aliases:
 - /desktop/extensions-sdk/extensions/validation/
 - /desktop/extensions-sdk/build/build-install/
 - /desktop/extensions-sdk/dev/cli/build-test-install-extension/
 - /desktop/extensions-sdk/extensions/validate/
weight: 20
---

Validate your extension before you share or publish it. Validating the extension ensures that the extension:

- Is built with the [image labels](labels.md) it requires to display correctly in the marketplace
- Installs and runs without problems

The Extensions CLI lets you validate your extension before installing and running it locally.

The validation checks if the extension’s `Dockerfile` specifies all the required labels and if the metadata file is valid against the JSON schema file.

To validate, run:

```console
$ docker extension validate <name-of-your-extension>
```

If your extension is valid, the following message displays:

```console
The extension image "name-of-your-extension" is valid
```

Before the image is built, it's also possible to validate only the `metadata.json` file:

```console
$ docker extension validate /path/to/metadata.json
```

The JSON schema used to validate the `metadata.json` file against can be found under the [releases page](https://github.com/docker/extensions-sdk/releases/latest).
