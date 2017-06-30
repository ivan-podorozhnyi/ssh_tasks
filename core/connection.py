from abc import ABC, abstractmethod
import paramiko
from core.user import SshUser


class Connection(ABC):
    @abstractmethod
    def connect(self):
        pass


class SshConnection:
    def __init__(self, user: SshUser):
        self.client = paramiko.SSHClient()
        self.user = user

    def connect_via_key(self):
        print('connecting')
        connection_data = self.user.make_connection_data()
        pkey = paramiko.RSAKey.from_private_key_file(connection_data["key"])
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=connection_data["hostname"],
                            username=connection_data["username"],
                            port=connection_data["port"],
                            pkey=pkey)
        return self

    def open_shell(self):
        print('invoking shell')
        return self.client.invoke_shell()

    def close(self):
        if self.client is not None:
            print('closing')
            self.client.close()

    def open_sftp(self):
        print('invoking sftp')
        return self.client.open_sftp()
