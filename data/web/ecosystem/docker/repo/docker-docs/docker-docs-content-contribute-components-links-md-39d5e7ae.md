---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/contribute/components/links.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.563679+00:00"
}
                    ---
                    # content/contribute/components/links.md

                    ---
description: components and formatting examples used in Docker's docs
title: Links
toc_max: 3
---

## Examples

[External links](https://docker.com) and [internal links](links.md) both
open in the same tab.

Use relative links, using source filenames.

#### Links to auto-generated content

When you link to heading IDs in auto-generated pages, such as CLI
reference content, you won't get any help from your editor in resolving the
anchor names. That's because the pages are generated at build-time and your
editor or LSP doesn't know about them in advance.

## Syntax

```md
[External links](https://docker.com)
[Internal links](links.md)
```
