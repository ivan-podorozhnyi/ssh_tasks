from core.user import SshUser
from core.connection import SshConnection
from core.cmd_handler import ShellCmdHandler
import pytest


@pytest.fixture(scope="module")
def connection(request):
    user = SshUser(name="anton", port=3022, key="../id_rsa",
                   address="127.0.0.1")
    connection = SshConnection(user).connect_via_key()

    def tear_down():
        connection.close()

    request.addfinalizer(tear_down)
    return connection


@pytest.fixture()
def shell(request, connection):
    shell = ShellCmdHandler(connection)

    def tear_down():
        shell.close()

    request.addfinalizer(tear_down)
    return shell


def test_read_man(shell):
    shell.send_command("man less\n")
    while True:
        stdout = shell.send_key("SPACE")
        if "AUTHOR" in stdout:
            break
    shell.send_command("q")
