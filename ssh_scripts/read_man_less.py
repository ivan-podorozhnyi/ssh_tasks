import paramiko

pkey = paramiko.RSAKey.from_private_key_file("/Users/akarab/.ssh/id_rsa")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="127.0.0.1", port=3022, username="anton", pkey=pkey)
channel = client.invoke_shell()

channel.send("man less\n")
stdout = ""
while stdout.find("AUTHOR") < 0:
    stdout = str(channel.recv(1024))
    channel.send(str(chr(32)))
channel.send("q")

channel.close()