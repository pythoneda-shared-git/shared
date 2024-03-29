# vim: set fileencoding=utf-8
"""
pythoneda/shared/git/ssh_git_repo.py

This file declares the SshGitRepo class.

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
from paramiko import RSAKey, AutoAddPolicy
from paramiko.agent import AgentRequestHandler, AgentServerProxy
from paramiko.client import SSHClient
from pythoneda.shared import attribute, BaseObject, sensitive


class SshVendor(BaseObject):
    """
    Represents a dulwich vendor to access Git repositories via SSH.

    Class name: SshVendor

    Responsibilities:
        - Configures dulwich so it can access remote Git repositories via SSH.

    Collaborators:
        - dulwich.porcelain: Acts as a client in need of SSH communications.
    """

    def __init__(
        self, sshUsername: str, privateKeyFile: str, privateKeyPassphrase: str
    ):
        """
        Creates a new SshVendor instance.
        :param sshUsername: The SSH username.
        :type sshUsername: str
        :param privateKeyFile: The private key for SSH authentication.
        :type privateKeyFile: str
        :param privateKeyPassphrase: The passphrase of the private key.
        :type privateKeyPassphrase: str
        """
        self._ssh_username = sshUsername
        self._private_key_file = privateKeyFile
        self._private_key_passphrase = privateKeyPassphrase
        self._ssh_kwargs = {"username": sshUsername}

    @property
    @attribute
    @sensitive
    def ssh_username(self) -> str:
        """
        Retrieves the SSH user name.
        :return: Such user name.
        :rtype: str
        """
        return self._ssh_username

    @property
    @attribute
    @sensitive
    def private_key_file(self) -> str:
        """
        Retrieves the location of the private key.
        :return: Such path.
        :rtype: str
        """
        return self._private_key_file

    @property
    @attribute
    @sensitive
    def private_key_passphrase(self) -> str:
        """
        Retrieves the private key passphrase.
        :return: Such value.
        :rtype: str
        """
        return self._private_key_passphrase

    def run_command(
        self, hostPath: str, command: str, username: str = None, password: str = None
    ):
        """
        Runs a command using SSH.
        :param hostPath: The host path.
        :type hostPath: str
        :param command: The command to run.
        :type command: str
        :param username: The username.
        :type username: str
        :param password: The password.
        :type password: str
        :return: A tuple consisting on the client and the session.
        :rtype: tuple
        """
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        pkey = RSAKey.from_private_key_file(
            self._private_key_file, password=self._private_key_passphrase
        )
        self.ssh_kwargs["pkey"] = pkey

        # Connect to the host
        client.connect(host_path, **self.ssh_kwargs)

        # Add the client's keys to the SSH agent
        agent = AgentServerProxy()
        AgentRequestHandler(agent)

        # Run the given command
        transport = client.get_transport()
        chan = transport.open_session()
        chan.exec_command(command)
        return client, chan

    def __call__(self, hostPath: str):
        """
        Performs an operation.
        :param hostPath: The host path.
        :type hostPath: str
        """
        client, chan = self.run_command(hostPath, "git-upload-pack /" + hostPath)
        return Protocol(lambda: chan.recv(65536), chan.sendall)
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
