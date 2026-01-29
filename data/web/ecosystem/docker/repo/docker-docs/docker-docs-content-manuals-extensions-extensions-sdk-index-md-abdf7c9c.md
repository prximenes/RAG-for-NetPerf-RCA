---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/extensions/extensions-sdk/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.900929+00:00"
}
                    ---
                    # content/manuals/extensions/extensions-sdk/_index.md

                    ---
title: Overview of the Extensions SDK
linkTitle: Extensions SDK
description: Overall index for Docker Extensions SDK documentation
keywords: Docker, Extensions, sdk
aliases:
 - /desktop/extensions-sdk/dev/overview/
 - /desktop/extensions-sdk/
grid:
  - title: "The build and publish process"
    description: Understand the process for building and publishing an extension.
    icon: "checklist"
    link: "/extensions/extensions-sdk/process/"
  - title: "Quickstart guide"
    description: Follow the quickstart guide to create a basic Docker extension quickly.
    icon: "explore"
    link: "/extensions/extensions-sdk/quickstart/"
  - title: "View the design guidelines"
    description: Ensure your extension aligns to Docker's design guidelines and principles.
    icon: "design_services"
    link: "/extensions/extensions-sdk/design/design-guidelines/"
  - title: "Publish your extension"
    description: Understand how to publish your extension to the Marketplace.
    icon: "publish"
    link: "/extensions/extensions-sdk/extensions/"
  - title: "Interacting with Kubernetes"
    description: Find information on how to interact indirectly with a Kubernetes cluster from your Docker extension.
    icon: "multiple_stop"
    link: "/extensions/extensions-sdk/guides/kubernetes/"
  - title: "Multi-arch extensions"
    description: Build your extension for multiple architectures.
    icon: "content_copy"
    link: "/extensions/extensions-sdk/extensions/multi-arch/"
---

The resources in this section help you create your own Docker extension.

The Docker CLI tool provides a set of commands to help you build and publish your extension, packaged as a 
specially formatted Docker image.

At the root of the image filesystem is a `metadata.json` file which describes the content of the extension. 
It's a fundamental element of a Docker extension.

An extension can contain a UI part and backend parts that run either on the host or in the Desktop virtual machine.
For further information, see [Architecture](architecture/_index.md).

You distribute extensions through Docker Hub. However, you can develop them locally without the need to push 
the extension to Docker Hub. See [Extensions distribution](extensions/DISTRIBUTION.md) for further details.

{{% include "extensions-form.md" %}}

{{< grid >}}
