---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/scout/integrations/team-collaboration/slack.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:13.131003+00:00"
}
                    ---
                    # content/manuals/scout/integrations/team-collaboration/slack.md

                    ---
title: Integrate Docker Scout with Slack
linkTitle: Slack
description: |
  Integrate Docker Scout with Slack to receive real-time updates
  about vulnerabilities and policy compliance in Slack channels
keywords: scout, team collaboration, slack, notifications, updates
---

You can integrate Docker Scout with Slack by creating a Slack webhook and
adding it to the Docker Scout Dashboard. Docker Scout will notify you about
when a new vulnerability is disclosed, and it affects one or more of your
images.

![Slack notification from Docker Scout](../../images/scout-slack-notification.png?border=true "Example Slack notification from Docker Scout")

## How it works

After configuring the integration, Docker Scout sends notifications about
changes to policy compliance and vulnerability exposure for your repositories,
to the Slack channels associated with the webhook.

> [!NOTE]
>
> Notifications are only triggered for the *last pushed* image tags for each
> repository. "Last pushed" refers to the image tag that was most recently
> pushed to the registry and analyzed by Docker Scout. If the last pushed image
> is not by a newly disclosed CVE, then no notification will be triggered.

For more information about Docker Scout notifications,
see [Notification settings](/manuals/scout/explore/dashboard.md#notification-settings)

## Setup

To add a Slack integration:

1. Create a webhook, see [Slack documentation](https://api.slack.com/messaging/webhooks).
2. Go to the [Slack integration page](https://scout.docker.com/settings/integrations/slack/) in the Docker Scout Dashboard.
3. In the **How to integrate** section, enter a **Configuration name**.
   Docker Scout uses this label as a display name for the integration,
   so you might want to change the default name into something more meaningful.
   For example the `#channel-name`, or the name of the team that this configuration belongs to.
4. Paste the webhook you just created in the **Slack webhook** field.

   Select the **Test webhook** button if you wish to verify the connection.
   Docker Scout will send a test message to the specified webhook.

5. Select whether you want to enable notifications for all your Scout-enabled image repositories,
   or enter the names of the repositories that you want to send notifications for.
6. When you're ready to enable the integration, select **Create**.

After creating the webhook, Docker Scout begins to send notifications updates
to the Slack channels associated with the webhook.

## Remove a Slack integration

To remove a Slack integration:

1. Go to the [Slack integration page](https://scout.docker.com/settings/integrations/slack/) in the Docker Scout Dashboard.
2. Select the **Remove** icon for the integration that you want to remove.
3. Confirm by selecting **Remove** again in the confirmation dialog.
