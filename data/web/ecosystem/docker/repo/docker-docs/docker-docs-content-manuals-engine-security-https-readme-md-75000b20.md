---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/engine/security/https/README.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.986170+00:00"
}
                    ---
                    # content/manuals/engine/security/https/README.md

                    ---
_build:
  list: never
  publishResources: false
  render: never
---

This is an initial attempt to make it easier to test the TLS (HTTPS) examples in the protect-access.md
doc.

At this point, it is a manual thing, and I've been running it in boot2docker.

My process is as following:

    $ boot2docker ssh
    root@boot2docker:/# git clone https://github.com/moby/moby
    root@boot2docker:/# cd docker/docs/articles/https
    root@boot2docker:/# make cert

lots of things to see and manually answer, as openssl wants to be interactive

> [!NOTE]: make sure you enter the hostname (`boot2docker` in my case) when prompted for `Computer Name`)

    root@boot2docker:/# sudo make run

Start another terminal:

    $ boot2docker ssh
    root@boot2docker:/# cd docker/docs/articles/https
    root@boot2docker:/# make client

The last connects first with `--tls` and then with `--tlsverify`, both should succeed.
