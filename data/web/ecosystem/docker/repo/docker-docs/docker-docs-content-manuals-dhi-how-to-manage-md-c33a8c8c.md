---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/dhi/how-to/manage.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:13.038665+00:00"
}
                    ---
                    # content/manuals/dhi/how-to/manage.md

                    ---
title: Manage Docker Hardened Images
linktitle: Manage images
description: Learn how to manage your mirrored and customized Docker Hardened Images in your organization.
keywords: manage docker hardened images, custom hardened images
weight: 35
---

{{< summary-bar feature_name="Docker Hardened Images" >}}

On the **Management** screen in Docker Hub, you can manage both your mirrored
Docker Hardened Image (DHI) repositories and customized DHI images in your
organization.

## Manage mirrored Docker Hardened Images

To manage your mirrored DHI repositories:

1. Go to the [Docker Hub](https://hub.docker.com) and sign in.
2. Select **My Hub**.
3. In the namespace drop-down, select your organization.
4. Select **Hardened Images** > **Management**.

   On this page, you can view your mirrored DHI
   repositories and view which source repositories they are mirrored from.

5. Select the menu icon in the far right column of the repository you want to manage.

   From here, you can:

   - **Customize**: Create a customized image based on the source repository.
   - **Stop mirroring**: Stop mirroring the DHI repository.

## Manage customized Docker Hardened Images

To manage your customized DHI repositories:

1. Go to [Docker Hub](https://hub.docker.com) and sign in.
2. Select **My Hub**.
3. In the namespace drop-down, select your organization.
4. Select **Hardened Images** > **Management**.
5. Select **Customizations**.

   On this page, you can view your customized DHI
   repositories.

6. Select the menu icon in the far right column of the repository you want to manage.

   From here, you can:

   - **Edit**: Edit the customized image.
   - **Create new**: Create a new customized image based on the source repository.
   - **Delete**: Delete the customized image.
