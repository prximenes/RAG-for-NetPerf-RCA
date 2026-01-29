---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/billing/_index.md",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.862711+00:00"
}
                    ---
                    # content/manuals/billing/_index.md

                    ---
title: Manage billing and payments
linkTitle: Billing
description: Find information about managing billing and payments for Docker subscriptions.
keywords: billing, invoice, payment, subscription, Docker billing, update payment method, billing history, invoices, payment verification, tax exemption
weight: 10
params:
  sidebar:
    group: Platform
grid_core:
- title: Add or update a payment method
  description: Learn how to add or update a payment method for your personal account or organization.
  link: /billing/payment-method/
  icon: credit_score
- title: Update billing information
  description: Discover how to update the billing information for your personal account or organization.
  link: /billing/details/
  icon: contract_edit
- title: View billing history
  description: Learn how to view billing history and download past invoices.
  link: /billing/history/
  icon: payments
- title: Billing FAQs
  description: Find the answers you need and explore common questions.
  link: /billing/faqs/
  icon: help
- title: Register a tax certificate
  description: Learn how to register a tax exemption certificate.
  link: /billing/tax-certificate/
  icon: developer_guide
- title: 3D Secure authentication
  description: Discover how Docker billing supports 3DS and how to troubleshoot potential issues.
  link: /billing/3d-secure/
  icon: wallet
aliases:
  - /billing/docker-hub-pricing/
---

Use the resources in this section to manage billing and payments for your Docker
subscriptions.

{{< grid items="grid_core" >}}
