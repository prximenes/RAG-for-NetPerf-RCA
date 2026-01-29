---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/extensions/extensions-sdk/dev/api/dashboard.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.915359+00:00"
}
                    ---
                    # content/manuals/extensions/extensions-sdk/dev/api/dashboard.md

                    ---
title: Dashboard
description: Docker extension API
keywords: Docker, extensions, sdk, API
aliases:
 - /desktop/extensions-sdk/dev/api/dashboard/
---

## User notifications

Toasts provide a brief notification to the user. They appear temporarily and
shouldn't interrupt the user experience. They also don't require user input to disappear.

### success

▸ **success**(`msg`): `void`

Use to display a toast message of type success.

```typescript
ddClient.desktopUI.toast.success("message");
```

### warning

▸ **warning**(`msg`): `void`

Use to display a toast message of type warning.

```typescript
ddClient.desktopUI.toast.warning("message");
```

### error

▸ **error**(`msg`): `void`

Use to display a toast message of type error.

```typescript
ddClient.desktopUI.toast.error("message");
```

For more details about method parameters and the return types available, see [Toast API reference](/reference/api/extensions-sdk/Toast.md).

> Deprecated user notifications
>
> These methods are deprecated and will be removed in a future version. Use the methods specified above.

```typescript
window.ddClient.toastSuccess("message");
window.ddClient.toastWarning("message");
window.ddClient.toastError("message");
```

## Open a file selection dialog

This function opens a file selector dialog that asks the user to select a file or folder.

▸ **showOpenDialog**(`dialogProperties`): `Promise`<[`OpenDialogResult`](/reference/api/extensions-sdk/OpenDialogResult.md)\>:

The `dialogProperties` parameter is a list of flags passed to Electron to customize the dialog's behaviour. For example, you can pass `multiSelections` to allow a user to select multiple files. See [Electron's documentation](https://www.electronjs.org/docs/latest/api/dialog) for a full list.

```typescript
const result = await ddClient.desktopUI.dialog.showOpenDialog({
  properties: ["openDirectory"],
});
if (!result.canceled) {
  console.log(result.paths);
}
```

## Open a URL

This function opens an external URL with the system default browser.

▸ **openExternal**(`url`): `void`

```typescript
ddClient.host.openExternal("https://docker.com");
```

> The URL must have the protocol `http` or `https`.

For more details about method parameters and the return types available, see [Desktop host API reference](/reference/api/extensions-sdk/Host.md).

> Deprecated user notifications
>
> This method is deprecated and will be removed in a future version. Use the methods specified above.

```typescript
window.ddClient.openExternal("https://docker.com");
```

## Navigation to Dashboard routes

From your extension, you can also [navigate](dashboard-routes-navigation.md) to other parts of the Docker Desktop Dashboard.
