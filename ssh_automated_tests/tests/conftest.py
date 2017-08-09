import pytest

from ssh_automated_tests.core.channel import SftpChannel
from ssh_automated_tests.core.connection import BaseSshConnection
from ssh_automated_tests.core.file import PropertiesFile
from ssh_automated_tests.core.shell import InteractiveShell
from ssh_automated_tests.core.user import ParamikoUserFromPropFile


@pytest.fixture(scope="module")
def connection(request):
    user = ParamikoUserFromPropFile(PropertiesFile('config'))

    connection = BaseSshConnection(user).connect()

    def tear_down():
        connection.disconnect()

    request.addfinalizer(tear_down)
    return connection


@pytest.fixture()
def shell(request, connection):
    shell = InteractiveShell(connection)

    def tear_down():
        shell.close()

    request.addfinalizer(tear_down)
    return shell


@pytest.fixture()
def sftp(request, connection):
    sftp = SftpChannel(connection)

    def tear_down():
        sftp.close()

    request.addfinalizer(tear_down)
    return sftp
