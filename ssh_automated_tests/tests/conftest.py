import pytest

from ssh_automated_tests.core.cmd_handler import ShellCmdHandler
from ssh_automated_tests.core.connection import SshConnection
from ssh_automated_tests.core.file import PropertiesFile
from ssh_automated_tests.core.user import ParamikoUserFromPropFile


@pytest.fixture(scope="module")
def connection(request):
    user = ParamikoUserFromPropFile(PropertiesFile('config'))

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
