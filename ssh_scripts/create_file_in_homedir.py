from core.user import SshUser
from core.connection import SshConnection
from core.cmd_handler import ShellCmdHandler


user = SshUser(name="anton", port=3022, key="../id_rsa", address="127.0.0.1")
connection = SshConnection(user).connect_via_key()
shell = ShellCmdHandler(connection)

shell.send_command("touch new_test111\n")

shell.close()
connection.close()
