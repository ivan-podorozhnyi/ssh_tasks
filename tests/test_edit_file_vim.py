import random
import string

import pytest

from core.cmd_handler import ShellCmdHandler, VimCmdHandler
from core.connection import SshConnection
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
def shell_handler(request, connection):
    handler = ShellCmdHandler(connection)

    def resource_teardown():
        handler.close()

    request.addfinalizer(resource_teardown)
    return handler


def test_edit_vim(shell_handler, connection):
    file_name = 'new_file.txt'
    random_text = ''.join(random.sample(string.digits, 8))
    vim_handler = VimCmdHandler(connection)
    vim_handler.edit_file(file_name, random_text)
    sftp_client = connection.open_sftp()
    remote_file = sftp_client.open('/home/ivan/' + file_name)
    file_content = ''
    for line in remote_file:
        file_content += line
    assert random_text in file_content
