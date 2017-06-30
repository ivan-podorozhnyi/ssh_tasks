from core.cmd_handler import ShellCmdHandler
from core.connection import SshConnection
from core.user import User
import pytest
import random, string


@pytest.fixture()
def setup_resource(request):
    user = User(name='ivan', port=3022, key='../id_rsa', address='127.0.0.1')
    connection = SshConnection(user)
    connection.connect()
    handler = ShellCmdHandler(connection)

    def teardown(setup_resource):
        setup_resource.close()
        connection.close()

    request.addfinalizer(teardown)
    return handler


def test_edit_vim(setup_resource):
    setup_resource.send_command('vim new_file.txt\n')
    setup_resource.send_command('i')
    random_text = ''.join(random.sample(string.digits, 8))
    setup_resource.send_command(random_text)
    setup_resource.send_command(str(chr(27)))
    setup_resource.send_command(':wq\n')

