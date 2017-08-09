from abc import ABC, abstractmethod

import paramiko

from ssh_automated_tests.core.user import User


class Connection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class SshConnection(Connection):
    @abstractmethod
    def open_shell(self):
        pass

    @abstractmethod
    def open_sftp(self):
        pass


class BaseSshConnection(SshConnection):
    def __init__(self, user: User):
        self._client = paramiko.SSHClient()
        self._user = user

    def connect(self):
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._client.connect(**self._user.connection_data())
        return self

    def open_shell(self):
        return self._client.invoke_shell()

    def open_sftp(self):
        return self._client.open_sftp()

    def disconnect(self):
        if self._client is not None:
            self._client.close()
