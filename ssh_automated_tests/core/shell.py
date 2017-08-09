from abc import ABC, abstractmethod
from time import sleep

from ssh_automated_tests.core.connection import BaseSshConnection


class Shell(ABC):
    @abstractmethod
    def execute(self, command: str):
        pass

    @abstractmethod
    def execute_with_output(self, command: str) -> str:
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def read_output(self) -> str:
        pass

    @abstractmethod
    def send_key(self, key: str):
        pass


class InteractiveShell(Shell):
    def __init__(self, connection: BaseSshConnection):
        self._connection = connection
        self._shell = self._connection.open_shell()

    def execute(self, command: str):
        self._shell.send(command)
        sleep(0.3)

    def execute_with_output(self, command: str) -> str:
        self._shell.send(command)
        sleep(0.3)
        return self.read_output()

    def read_output(self) -> str:
        stdout_raw = b""
        while self._shell.recv_ready():
            stdout_raw += self._shell.recv(1024)
        return str(stdout_raw, "utf-8")

    def send_key(self, key: str):
        if key == 'ESC':
            return self.execute_with_output(str(chr(27)))
        elif key == 'SPACE':
            return self.execute_with_output(str(chr(32)))

    def close(self):
        if self._shell is not None:
            self._shell.close()