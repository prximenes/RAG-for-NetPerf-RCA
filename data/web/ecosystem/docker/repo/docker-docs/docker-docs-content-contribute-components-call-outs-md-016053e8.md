---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/contribute/components/call-outs.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.563188+00:00"
}
                    ---
                    # content/contribute/components/call-outs.md

                    ---
description: components and formatting examples used in Docker's docs
title: Callouts
toc_max: 3
---

We support these broad categories of callouts:

- Alerts: Note, Tip, Important, Warning, Caution

We also support summary bars, which represent a feature's required subscription, version, or Adminstrator role.
To add a summary bar:

Add the feature name to the `/data/summary.yaml` file. Use the following attributes:

| Attribute      | Description                                            | Possible values                                         |
|----------------|--------------------------------------------------------|---------------------------------------------------------|
| `subscription` | Notes the subscription required to use the feature     | All, Personal, Pro, Team, Business                      |
| `availability` | Notes what product development stage the feature is in | Experimental, Beta, Early Access, GA, Retired           |
| `requires`     | Notes what minimum version is required for the feature | No specific value, use a string to describe the version and link to relevant release notes |
| `for`          | Notes if the feature is intended for IT Administrators | Administrators                                          |

Then, add the `summary-bar` shortcode on the page you want to add the summary bar to. Note, the feature name is case sensitive. The icons that appear in the summary bar are automatically rendered.

## Examples

{{< summary-bar feature_name="PKG installer" >}}

> [!NOTE]
>
> Note the way the `get_hit_count` function is written. This basic retry
> loop lets us attempt our request multiple times if the redis service is
> not available. This is useful at startup while the application comes
> online, but also makes our application more resilient if the Redis
> service needs to be restarted anytime during the app's lifetime. In a
> cluster, this also helps handling momentary connection drops between
> nodes.

> [!TIP]
>
> For a smaller base image, use `alpine`.

> [!IMPORTANT]
>
> Treat access tokens like your password and keep them secret. Store your
> tokens securely (for example, in a credential manager).

> [!WARNING]
>
> Removing Volumes
>
> By default, named volumes in your compose file are NOT removed when running
> `docker compose down`. If you want to remove the volumes, you will need to add
> the `--volumes` flag.
>
> The Docker Desktop Dashboard does not remove volumes when you delete the app stack.

> [!CAUTION]
>
> Here be dragons.

For both of the following callouts, consult [the Docker release lifecycle](/release-lifecycle) for more information on when to use them.

## Formatting

```md
{{</* summary-bar feature_name="PKG installer" */>}}
```

```html
> [!NOTE]
>
> Note the way the `get_hit_count` function is written. This basic retry
> loop lets us attempt our request multiple times if the redis service is
> not available. This is useful at startup while the application comes
> online, but also makes our application more resilient if the Redis
> service needs to be restarted anytime during the app's lifetime. In a
> cluster, this also helps handling momentary connection drops between
> nodes.

> [!TIP]
>
> For a smaller base image, use `alpine`.

> [!IMPORTANT]
>
> Treat access tokens like your password and keep them secret. Store your
> tokens securely (for example, in a credential manager).

> [!WARNING]
>
> Removing Volumes
>
> By default, named volumes in your compose file are NOT removed when running
> `docker compose down`. If you want to remove the volumes, you will need to add
> the `--volumes` flag.
>
> The Docker Desktop Dashboard does not remove volumes when you delete the app stack.

> [!CAUTION]
>
> Here be dragons.
```
