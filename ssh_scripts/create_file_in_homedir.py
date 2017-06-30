import paramiko


key = paramiko.RSAKey.from_private_key_file("/Users/akarab/.ssh/id_rsa")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("connecting")
client.connect(hostname="127.0.0.1", port=3022, username="anton", pkey=key)
print("Connected")

stdin, stdout, stderr = client.exec_command("touch test_file")
print([line for line in stderr.readlines()])
stdin, stdout, stderr = client.exec_command("ls")
print([line for line in stdout.readlines()])

client.close()