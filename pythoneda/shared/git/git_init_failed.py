# vim: set fileencoding=utf-8
"""
pythoneda/shared/git/git_init_failed.py

This file defines the GitInitFailed exception class.

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
from pythoneda.shared import BaseObject


class GitInitFailed(Exception, BaseObject):
    """
    git init failed.

    Class name: GitInitFailed

    Responsibilities:
        - Represent an error when initializing a git repository.

    Collaborators:
        - None
    """

    def __init__(self, folder: str, output: str):
        """
        Creates a new instance.
        :param folder: The repository folder.
        :type folder: str
        :param output: The output of the git init command.
        :type output: str
        """
        super().__init__(f'"git init" failed (in {folder})')
        self._output = output

    @property
    def output(self) -> str:
        """
        Retrieves the output of the command.
        :return: Such output.
        :rtype: str
        """
        return self._output
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
