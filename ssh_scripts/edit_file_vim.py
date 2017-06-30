import paramiko
import time

host = '127.0.0.1'
user = 'ivan'
secret = '123'
port = 3022


k = paramiko.RSAKey.from_private_key_file("../id_rsa")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting")
client.connect(hostname=host, port=port, username=user, pkey=k)

channel = client.invoke_shell()
channel.send('vim ha.txt\n')

channel.send('i')

text = input('\tPlease enter text: ')
channel.send(text)
# channel.send('\x1b')
channel.send(str(chr(27)))

channel.send(':wq\n')


channel.close()
client.close()
