---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/ai/cagent/reference/examples.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.897309+00:00"
}
                    ---
                    # content/manuals/ai/cagent/reference/examples.md

                    ---
title: Examples
description: Get inspiration from agent examples
keywords: [ai, agent, cagent]
weight: 40
---

Get inspiration from the following agent examples.
See more examples in the [cagent GitHub repository](https://github.com/docker/cagent/tree/main/examples).

## Development team

{{% cagent-example.inline "dev-team.yaml" %}}
{{- $example := .Get 0 }}
{{- $baseUrl := "https://raw.githubusercontent.com/docker/cagent/refs/heads/main/examples" }}
{{- $url := fmt.Printf "%s/%s" $baseUrl $example }}
{{- with resources.GetRemote $url }}
{{ $data := .Content | transform.Unmarshal }}

```yaml {collapse=true}
{{ .Content }}
```

{{ end }}
{{% /cagent-example.inline %}}

## Go developer

{{% cagent-example.inline "gopher.yaml" /%}}

## Technical blog writer

{{% cagent-example.inline "blog.yaml" /%}}
