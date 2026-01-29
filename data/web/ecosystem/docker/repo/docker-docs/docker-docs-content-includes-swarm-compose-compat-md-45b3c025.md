---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/includes/swarm-compose-compat.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.525013+00:00"
}
                    ---
                    # content/includes/swarm-compose-compat.md

                    > [!NOTE]
>
> The `docker stack deploy` command uses the legacy
> [Compose file version 3](/reference/compose-file/legacy-versions/)
> format, used by Compose V1. The latest format, defined by the
> [Compose specification](/reference/compose-file/)
> isn't compatible with the `docker stack deploy` command.
>
> For more information about the evolution of Compose, see
> [History of Compose](/compose/history/).
