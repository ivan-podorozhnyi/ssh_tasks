from abc import ABC, abstractmethod

import paramiko

from core.user import User


class Connection(ABC):

    @abstractmethod
    def connect(self):
        pass


class SshConnection:
    def __init__(self, user: User):
        self.client = paramiko.SSHClient()
        self.key = paramiko.RSAKey.from_private_key_file(user.key)
        self.user = user

    def connect(self):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.user.address, username=self.user.name, port=self.user.port, pkey=self.key)

    def open_shell(self):
        return self.client.invoke_shell()

    def close(self):
        if self.client is not None:
            self.client.close()
