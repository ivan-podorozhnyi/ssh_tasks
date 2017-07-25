from abc import ABC, abstractmethod

from ssh_automated_tests.core.connection import Connection


class Channel(ABC):
    @abstractmethod
    def open_file(self, file_name: str):
        pass

    @abstractmethod
    def close(self):
        pass


class SftpChannel(Channel):
    def __init__(self, connection: Connection):
        self._connection = connection
        self._sftp = self._initialize_sftp()

    def _initialize_sftp(self):
        try:
            return self._connection.open_sftp()
        except AttributeError:
            raise AttributeError("Given connection can't establish sftp "
                                 "channel.")

    def get_file_stat(self, file_name: str):
        return self._sftp.stat(file_name)

    def open_file(self, file_name: str):
        return self._sftp.open(file_name)

    def close(self):
        if self._sftp is not None:
            self._sftp.close()