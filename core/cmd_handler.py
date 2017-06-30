from abc import ABC, abstractmethod

from time import sleep
from core.connection import Connection, SshConnection
import paramiko


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
