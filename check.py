from core.cmd_handler import ShellCmdHandler
from core.connection import SshConnection
from core.user import SshUser

user = SshUser(name='ivan', port=3022, key='id_rsa', address='127.0.0.1')
connection = SshConnection(user)
connection.connect_via_key()
handler = ShellCmdHandler(connection)
handler.send_command('touch b_file.txt')
handler.close()
connection.close()
