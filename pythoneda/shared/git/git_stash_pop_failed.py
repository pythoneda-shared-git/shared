"""
pythoneda/shared/git/git_stash_pop_failed.py

This file defines the GitStashPopFailed exception class.

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
from pythoneda import BaseObject


class GitStashPopFailed(Exception, BaseObject):
    """
    Running git stash pop failed.

    Class name: GitStashPopFailed

    Responsibilities:
        - Represent the error when running git stash pop.

    Collaborators:
        - None
    """

    def __init__(self, folder: str):
        """
        Creates a new instance.
        :param folder: The folder with the cloned repository.
        :type folder: str
        """
        super().__init__(f'"git stash pop" in folder {folder} failed')
