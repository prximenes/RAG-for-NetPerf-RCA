---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/includes/buildx-v0.10-disclaimer.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.521463+00:00"
}
                    ---
                    # content/includes/buildx-v0.10-disclaimer.md

                    > [!NOTE]
>
> Buildx v0.10 enables support for a minimal [SLSA Provenance](https://slsa.dev/provenance/)
> attestation, which requires support for [OCI-compliant](https://github.com/opencontainers/image-spec)
> multi-platform images. This may introduce issues with registry and runtime support
> (e.g. [Google Cloud Run and AWS Lambda](https://github.com/docker/buildx/issues/1533)).
> You can optionally disable the default provenance attestation functionality
> using `--provenance=false`.
