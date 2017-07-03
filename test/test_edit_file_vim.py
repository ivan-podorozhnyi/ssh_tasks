import random
import string

import pytest

from core.cmd_handler import VimCmdHandler
from core.connection import SshConnection
from core.file_generator import RemoteHomeFileGenerator, TxtFileGenerator
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


def test_edit_vim(connection):
    new_txt_file = TxtFileGenerator('new_file')
    new_remote_file = RemoteHomeFileGenerator(new_txt_file, 'ivan')
    random_text = RandomGenerator(10).generate_string('digits')
    vim_handler = VimCmdHandler(connection)
    vim_handler.edit_file(new_txt_file.get_name(), random_text)
    sftp_client = connection.open_sftp()
    remote_file = sftp_client.open(new_remote_file.get_name())
    file_content = ''
    for line in remote_file:
        file_content += line
    assert random_text in file_content
