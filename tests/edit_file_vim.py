from core.cmd_handler import ShellCmdHandler
from core.connection import SshConnection
from core.user import SshUser

user = SshUser(name='ivan', port=3022, key='../id_rsa', address='127.0.0.1')
connection = SshConnection(user)
connection.connect_via_key()
handler = ShellCmdHandler(connection)
handler.send_command('vim new_file.txt\n')
handler.send_command('i')
text = input('\tPlease enter text: ')
handler.send_command(text)
handler.send_command(str(chr(27)))
handler.send_command(':wq\n')

handler.close()
connection.close()
