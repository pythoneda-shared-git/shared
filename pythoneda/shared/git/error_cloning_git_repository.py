# vim: set fileencoding=utf-8
"""
pythoneda/shared/git/error_cloning_git_repository.py

This file defines the ErrorCloningGitRepository exception class.

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


class ErrorCloningGitRepository(Exception, BaseObject):
    """
    Running git clone [url] failed.

    Class name: ErrorCloningGitRepository

    Responsibilities:
        - Represent the error running git clone.

    Collaborators:
        - None
    """

    def __init__(self, url: str, folder: str):
        """
        Creates a new instance.
        :param url: The url of the repository.
        :type url: str
        :param folder: The folder where the repository was being cloned.
        :type folder: str
        """
        super().__init__('"git clone {url}" in folder {folder} failed')
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
