import paramiko

host = '127.0.0.1'
user = 'ivan'
secret = '123'
port = 3022

k = paramiko.RSAKey.from_private_key_file("../id_rsa")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, port=port, username=user, pkey=k)

sftp_client = client.open_sftp()
remote_file = sftp_client.open('/etc/hosts')
text_search = '127.0.0.1\tlocalhost'

try:
    for line in remote_file:
        if text_search in line:
            print('yes')
finally:
    remote_file.close()
