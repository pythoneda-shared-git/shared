"""
pythoneda/shared/git/git_push_branch_failed.py

This file defines the GitPushBranchFailed exception class.

Copyright (C) 2023-today rydnr's pythoneda-shared-git/shared

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


class GitPushBranchFailed(Exception):
    """
    Running git push [branch] failed.

    Class name: GitPushBranchFailed

    Responsibilities:
        - Represent the error when running git push [branch].

    Collaborators:
        - None
    """

    def __init__(self, folder: str, branch: str):
        """
        Creates a new GitPushBranch instance.
        :param folder: The folder with the cloned repository.
        :type folder: str
        :param branch: The branch.
        :type branch: str
        """
        super().__init__(f'"git push {branch}" in folder {folder} failed')
