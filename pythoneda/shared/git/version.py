"""
pythoneda/shared/git/version.py

This file declares the Version class.

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
from pythoneda import attribute, ValueObject
import semver

class Version(ValueObject):
    """
    Represents a version.

    Class name: Version

    Responsibilities:
        - Represents a version.
        - Knows how to create new versions.

    Collaborators:
        - None
    """

    def __init__(self, version: str):
        """
        Creates a new Version instance.
        :param version: The version.
        :type version: str
        """
        super().__init__()
        self._value = version

    @property
    @attribute
    def value(self) -> str:
        """
        Retrieves the version.
        :return: Such value.
        :rtype: str
        """
        return self._value

    def increase_major(self): # -> Version:
        """
        Increases the major value.
        :return: The new version.
        :rtype: Version
        """
        version = semver.Version.parse(self.value)

        return Version(str(version.bump_major()))

    def increase_minor(self): # -> Version:
        """
        Increases the minor value.
        :return: The new version.
        :rtype: Version
        """
        version = semver.Version.parse(self.value)

        return Version(str(version.bump_minor()))

    def increase_patch(self): # -> Version:
        """
        Increases the patch value.
        :return: The new version.
        :rtype: Version
        """
        version = semver.Version.parse(self.value)

        return Version(str(version.bump_patch()))

    def increase_prerelease(self): # -> Version:
        """
        Increases the prerelease value.
        :return: The new version.
        :rtype: Version
        """
        version = semver.Version.parse(self.value)

        return Version(str(version.bump_prerelease()))

    def increase_build(self): # -> Version:
        """
        Increases the build value.
        :return: The new version.
        :rtype: Version
        """
        version = semver.Version.parse(self.value)

        return Version(str(version.bump_build()))
