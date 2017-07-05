import pytest

from core.connection import SshConnection
from core.file_handler import NoExtensionFileHandler
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


def test_find_string(sftp_client):
    new_file = NoExtensionFileHandler('/etc/hosts')
    remote_file = sftp_client.open(new_file.get_name())
    searchable_string = '127.0.0.1\tlocalhost'
    file_content = ''
    for line in remote_file:
        file_content += line
    assert searchable_string in file_content
