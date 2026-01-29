---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/includes/compose/services-networks.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.767972+00:00"
}
                    ---
                    # content/includes/compose/services-networks.md

                    The `networks` attribute defines the networks that service containers are attached to, referencing entries under the
`networks` top-level element. The `networks` attribute helps manage the networking aspects of containers, providing control over how services are segmented and interact within the Docker environment. This is used to specify which networks the containers for that service should connect to. This is important for defining how containers communicate with each other and externally.
