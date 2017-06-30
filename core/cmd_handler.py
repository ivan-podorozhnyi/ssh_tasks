from abc import ABC, abstractmethod
from time import sleep

from core.connection import SshConnection


class CmdHandler(ABC):
    @abstractmethod
    def send_command(self, command):
        pass


class ShellCmdHandler(CmdHandler):
    def __init__(self, connection: SshConnection):
        self.connection = connection
        self.shell = self.connection.open_shell()

    def send_command(self, command):
        self.shell.send(command)
        sleep(0.5)

    def close(self):
        self.shell.close()

    def send_key(self, key: str):
        if key == 'ESC':
            self.send_command(str(chr(27)))
        elif key == 'SPACE':
            self.send_command(str(chr(32)))


class VimCmdHandler(ShellCmdHandler):
    def __init__(self, connection: SshConnection):
        super().__init__(connection)

    def edit_file(self, file_name):
        self.send_command('vim ' + file_name + '\n')
