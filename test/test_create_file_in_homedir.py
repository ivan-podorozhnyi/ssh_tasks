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

@pytest.fixture()
def sftp(request, connection):
    sftp = connection.open_sftp()

    def tear_down():
        sftp.close()

    request.addfinalizer(tear_down)
    return sftp


def test_create_file(shell, sftp):
    file_name = "new_test1235252"

    shell.send_command("touch {}\n".format(file_name))
    sftp.stat(file_name)
