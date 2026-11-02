---
okf_version: "0.2"
---

# pythoneda-shared-git/shared

* [Github shared kernel](pythoneda-shared-git-shared.md) - Shared Kernel: This package provides a reusable model of git concepts.

## Adapter
* [GitProgressLogging](git-progress-logging.md) - Shows the progress of long-running git operations.
* [SshVendor](ssh-vendor.md) - Represents a dulwich vendor to access Git repositories via SSH.

## Entity
* [GitRepo](git-repo.md) - Represents a Git repository.

## Value Object
* [ErrorCloningGitRepository](error-cloning-git-repository.md) - Running git clone [url] failed.
* [GitAdd](git-add.md) - Provides git add operations.
* [GitAddAllFailed](git-add-all-failed.md) - Adding all changes to the git repository failed.
* [GitAddFailed](git-add-failed.md) - Adding a file to the git repository failed.
* [GitApply](git-apply.md) - Provides git apply operations.
* [GitApplyFailed](git-apply-failed.md) - Running git apply failed.
* [GitBranch](git-branch.md) - Models branches in git.
* [GitBranchFailed](git-branch-failed.md) - Running git branch failed.
* [GitBranchUnsetUpstreamFailed](git-branch-unset-upstream-failed.md) - Running git branch --unset-upstream failed.
* [GitCheckAttr](git-check-attr.md) - Provides git check-attr operations.
* [GitCheckAttrAllFailed](git-check-attr-all-failed.md) - Retrieving the metadata of a file failed.
* [GitCheckAttrFailed](git-check-attr-failed.md) - Retrieving the value of a metadata attribute of a file failed.
* [GitCheckout](git-checkout.md) - Provides git checkout operations.
* [GitCheckoutFailed](git-checkout-failed.md) - Running git checkout [rev] failed.
* [GitClone](git-clone.md) - Clones git repositories.
* [GitCloneFailed](git-clone-failed.md) - Running git clone failed.
* [GitCommit](git-commit.md) - Models commits in git.
* [GitCommitFailed](git-commit-failed.md) - Running git commit failed.
* [GitDiff](git-diff.md) - Provides git diff operations.
* [GitDiffFailed](git-diff-failed.md) - Running git diff failed.
* [GitInit](git-init.md) - Provides git init operations.
* [GitInitFailed](git-init-failed.md) - git init failed.
* [GitOperation](git-operation.md) - Common logic for git operations.
* [GitPush](git-push.md) - Provides git push operations.
* [GitPushBranchFailed](git-push-branch-failed.md) - Running git push [branch] failed.
* [GitPushFailed](git-push-failed.md) - Running git push failed.
* [GitPushTagsFailed](git-push-tags-failed.md) - Running git push --tags failed.
* [GitRemote](git-remote.md) - Models remotes in git.
* [GitRemoteAddFailed](git-remote-add-failed.md) - Running git remote add failed.
* [GitStash](git-stash.md) - Provides git stash operations.
* [GitStashPopFailed](git-stash-pop-failed.md) - Running git stash pop failed.
* [GitStashPushFailed](git-stash-push-failed.md) - Running git stash push failed.
* [GitTag](git-tag.md) - Provides git operations related to tags.
* [GitTagFailed](git-tag-failed.md) - Running git tag [tag] failed.
* [InvalidGithubCredentials](invalid-github-credentials.md) - Access to GitHub API was denied.
* [SshGitRepo](ssh-git-repo.md) - Represents a Git repository accessed via SSH.
* [SshPrivateKeyGitPolicy](ssh-private-key-git-policy.md) - A policy to use a private key for git operations over ssh.
* [Version](version.md) - Represents a version.
