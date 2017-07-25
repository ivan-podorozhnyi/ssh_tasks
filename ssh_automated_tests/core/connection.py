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
    def __init__(self, user: User):
        self._client = paramiko.SSHClient()
        self._user = user

    def connect(self):
        print('connecting')
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._client.connect(**self._user.connection_data())
        return self

    def open_shell(self):
        print('invoking shell')
        return self._client.invoke_shell()

    def open_sftp(self):
        print('invoking sftp')
        return self._client.open_sftp()

    def disconnect(self):
        if self._client is not None:
            print('closing')
            self._client.close()
