---
type: Adapter
title: "SshVendor"
description: "Represents a dulwich vendor to access Git repositories via SSH."
resource: https://github.com/pythoneda-shared-git/shared/blob/main/pythoneda/shared/git/ssh_vendor.py
tags: [domain]
generated: { by: pythoneda-grill/deepseek-v4-pro, at: 2026-11-02T19:55:27Z }
sources:
  - id: src
    resource: https://github.com/pythoneda-shared-git/shared/blob/main/pythoneda/shared/git/ssh_vendor.py
    title: pythoneda/shared/git/ssh_vendor.py
  - id: readme
    resource: https://github.com/pythoneda-shared-git/shared/blob/main/README.md
    title: README.md
status: draft
---

Represents a dulwich vendor to access Git repositories via SSH.

Class name: SshVendor

Responsibilities:
    - Configures dulwich so it can access remote Git repositories via SSH.

Collaborators:
    - dulwich.porcelain: Acts as a client in need of SSH communications.
