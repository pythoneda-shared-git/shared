# vim: set fileencoding=utf-8
"""
pythoneda/shared/git/git_remote.py

This file declares the GitRemote class.

Copyright (C) 2024-today rydnr's pythoneda-shared-git/shared

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
from .git_remote_add_failed import GitRemoteAddFailed
from .git_operation import GitOperation


class GitRemote(GitOperation):
    """
    Models remotes in git.

    Class name: GitRemote

    Responsibilities:
        - Performs "git remote" operations.

    Collaborators:
        - None
    """

    def __init__(self, folder: str):
        """
        Creates a new GitRemote instance for given folder.
        :param folder: The cloned repository.
        :type folder: str
        """
        super().__init__(folder)

    async def add(self, url: str, remote: str = "origin"):
        """
        Creates a new remote.
        :param url: The url of the remote.
        :type url: str
        :param remote: The name of the remote.
        :type remote: str
        """
        (code, stdout, stderr) = await self.run(["git", "remote", "add", remote, url])
        if code != 0:
            if stderr != "":
                GitRemote.logger().error(stderr)
            if stdout != "":
                GitRemote.logger().error(stdout)
            raise GitRemoteAddFailed(self.folder, url, remote, stderr)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
