---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/contribute/components/images.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.560299+00:00"
}
                    ---
                    # content/contribute/components/images.md

                    ---
description: components and formatting examples used in Docker's docs
title: Images
toc_max: 3
---

## Example

- A small image: ![a small image](/assets/images/footer_moby_icon.png)

- Large images occupy the full width of the reading column by default:

  ![a pretty wide image](/assets/images/banner_image_24512.png)

- Image size can be set using query parameters: `?h=<height>&w=<width>`

  ![a pretty wide image](/assets/images/banner_image_24512.png?w=100&h=50)

- Image with a border, also set with a query parameter: `?border=true`

  ![a small image](/assets/images/footer_moby_icon.png?border=true)


## HTML and Markdown

```markdown
- A small image: ![a small image](/assets/images/footer_moby_icon.png)

- Large images occupy the full width of the reading column by default:

  ![a pretty wide image](/assets/images/banner_image_24512.png)

- Image size can be set using query parameters: `?h=<height>&w=<width>`

  ![a pretty wide image](/assets/images/banner_image_24512.png?w=100&h=50)

- Image with a border, also set with a query parameter: `?border=true`

  ![a small image](/assets/images/footer_moby_icon.png?border=true)
```
