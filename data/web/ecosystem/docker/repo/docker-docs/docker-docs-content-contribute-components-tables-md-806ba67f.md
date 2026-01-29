---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/contribute/components/tables.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.560843+00:00"
}
                    ---
                    # content/contribute/components/tables.md

                    ---
description: components and formatting examples used in Docker's docs
title: Tables
toc_max: 3
---

## Example

### Basic table

| Permission level                                                         | Access                                                        |
| :----------------------------------------------------------------------- | :------------------------------------------------------------ |
| **Bold** or _italic_ within a table cell. Next cell is empty on purpose. |                                                               |
|                                                                          | Previous cell is empty. A `--flag` in mono text.              |
| Read                                                                     | Pull                                                          |
| Read/Write                                                               | Pull, push                                                    |
| Admin                                                                    | All of the above, plus update description, create, and delete |

### Feature-support table

| Platform   | x86_64 / amd64 |
| :--------- | :------------: |
| Ubuntu     |       ✅       |
| Debian     |       ✅       |
| Fedora     |                |
| Arch (btw) |       ✅       |

## Markdown

### Basic table

```md
| Permission level                                                         | Access                                                        |
| :----------------------------------------------------------------------- | :------------------------------------------------------------ |
| **Bold** or _italic_ within a table cell. Next cell is empty on purpose. |                                                               |
|                                                                          | Previous cell is empty. A `--flag` in mono text.              |
| Read                                                                     | Pull                                                          |
| Read/Write                                                               | Pull, push                                                    |
| Admin                                                                    | All of the above, plus update description, create, and delete |
```

The alignment of the cells in the source doesn't really matter. The ending pipe
character is optional (unless the last cell is supposed to be empty).

### Feature-support table

```md
| Platform   | x86_64 / amd64 |
| :--------- | :------------: |
| Ubuntu     |       ✅       |
| Debian     |       ✅       |
| Fedora     |                |
| Arch (btw) |       ✅       |
```
