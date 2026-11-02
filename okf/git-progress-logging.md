---
type: Adapter
title: "GitProgressLogging"
description: "Shows the progress of long-running git operations."
resource: https://github.com/pythoneda-shared-git/shared/blob/main/pythoneda/shared/git/git_progress_logging.py
tags: [domain]
generated: { by: pythoneda-grill/deepseek-v4-pro, at: 2026-11-02T19:55:27Z }
sources:
  - id: src
    resource: https://github.com/pythoneda-shared-git/shared/blob/main/pythoneda/shared/git/git_progress_logging.py
    title: pythoneda/shared/git/git_progress_logging.py
  - id: readme
    resource: https://github.com/pythoneda-shared-git/shared/blob/main/README.md
    title: README.md
status: draft
---

Shows the progress of long-running git operations.

Class name: GitProgressLogging

Responsibilities:
    - Logs the progress of git operations.

Collaborators:
    - GitRepo: Uses me for certain git operations.
