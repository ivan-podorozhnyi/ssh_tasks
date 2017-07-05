import pytest

from core.cmd_handler import VimCmdHandler
from core.connection import SshConnection
from core.file_handler import RemoteHomeFileHandler, TxtFileHandler
from core.random_generator import RandomGenerator
from core.user import SshUser


@pytest.fixture()
def connection(request):
    user = SshUser(name='ivan', port=3022, key='../id_rsa', address='127.0.0.1')
    ssh_connection = SshConnection(user)
    ssh_connection.connect_via_key()

    def teardown():
        ssh_connection.close()

    request.addfinalizer(teardown)
    return ssh_connection


@pytest.fixture()
def sftp_client(request, connection):
    client = connection.open_sftp()

    def teardown():
        client.close()

    request.addfinalizer(teardown)
    return client


def test_edit_vim(connection, sftp_client):
    txt_file = TxtFileHandler('new_file')
    remote_file = RemoteHomeFileHandler(txt_file, 'ivan')
    random_text = RandomGenerator(10).generate_string('digits')
    vim_handler = VimCmdHandler(connection)
    vim_handler.edit_file(txt_file.get_name(), random_text)
    remote_file = sftp_client.open(remote_file.get_name())
    file_content = ''
    for line in remote_file:
        file_content += line
    assert random_text in file_content
