---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/docker-hub/repos/create.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:13.170490+00:00"
}
                    ---
                    # content/manuals/docker-hub/repos/create.md

                    ---
description: Learn how to create a repository on Docker Hub
keywords: Docker Hub, Hub, repositories, create
title: Create a repository
linkTitle: Create
toc_max: 3
weight: 20
---

1. Sign in to [Docker Hub](https://hub.docker.com).
2. Select **My Hub** > **Repositories**.
3. Near the top-right corner, select **Create repository**.
4. Select a **Namespace**.

   You can choose to locate it under your own user account, or under any
   organization where you are an owner or editor.

5. Specify the **Repository Name**.

   The repository name needs to:
    - Be unique
    - Have between 2 and 255 characters
    - Only contain lowercase letters, numbers, hyphens (`-`), and underscores
      (`_`)

   > [!NOTE]
   >
   > You can't rename a Docker Hub repository once it's created.

6. Specify the **Short description**.

   The description can be up to 100 characters. It appears in search results.

7. Select the default visibility.

   - **Public**: The repository appears in Docker Hub search results and can be
     pulled by everyone.
   - **Private**: The repository doesn't appear in Docker Hub search results and
     is only accessible to you and collaborators. In addition, if you selected
     an organization's namespace, then the repository is accessible to those
     with applicable roles or permissions. For more details, see [Roles and
     permissions](/manuals/enterprise/security/roles-and-permissions.md).

   > [!NOTE]
   >
   > For organizations creating a new repository, if you're unsure which
   > visibility to choose, then Docker recommends that you select **Private**.

8. Select **Create**.

After the repository is created, the **General** page appears. You are now able to manage:

- [Repository information](./manage/information.md)
- [Access](./manage/access.md)
- [Images](./manage/hub-images/_index.md)
- [Automated builds](./manage/builds/_index.md)
- [Webhooks](./manage/webhooks.md)
- [Image security insights](./manage/vulnerability-scanning.md)
