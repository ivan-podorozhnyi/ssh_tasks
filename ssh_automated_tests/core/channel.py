from abc import ABC, abstractmethod

from ssh_automated_tests.core.connection import SshConnection


class FileChannel(ABC):
    @abstractmethod
    def open(self, file_name: str):
        pass

    @abstractmethod
    def get_stat(self, file_name: str):
        pass

    @abstractmethod
    def close(self):
        pass


class SftpChannel(FileChannel):
    def __init__(self, connection: SshConnection):
        self._connection = connection
        self._sftp = self._connection.open_sftp()

    def get_stat(self, file_name: str):
        return self._sftp.stat(file_name)

    def open(self, file_name: str):
        return self._sftp.open(file_name)

    def close(self):
        if self._sftp is not None:
            self._sftp.close()