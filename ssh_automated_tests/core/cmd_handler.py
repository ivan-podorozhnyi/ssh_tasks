from abc import ABC, abstractmethod
from time import sleep

from ssh_automated_tests.core.connection import SshConnection


class CmdHandler(ABC):
    @abstractmethod
    def send_command(self, command):
        pass


class ShellCmdHandler(CmdHandler):
    def __init__(self, connection: SshConnection):
        self.connection = connection
        self._shell = self.connection.open_shell()

    def send_command(self, command):
        self._shell.send(command)
        sleep(0.1)
        return self.read_output()

    def read_output(self):
        stdout_raw = b""
        while self._shell.recv_ready():
            stdout_raw += self._shell.recv(1024)
        return str(stdout_raw, "utf-8")

    def close(self):
        self._shell.close()

    def send_key(self, key: str):
        if key == 'ESC':
            return self.send_command(str(chr(27)))
        elif key == 'SPACE':
            return self.send_command(str(chr(32)))


class VimCmdHandler(ShellCmdHandler):
    def __init__(self, connection: SshConnection):
        super().__init__(connection)

    def edit_file(self, file_name, text):
        self.send_command('vim ' + file_name + '\n')
        self.send_command('i')
        self.send_command(text)
        super().send_key('ESC')
        super().send_command(':wq\n')

