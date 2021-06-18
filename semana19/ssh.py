import paramiko, sys

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

hostname = '192.168.0.167'
username = 'orlando'
password = '123mudar'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect(hostname, username=username, password=password)

channel = client.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')

stdin.write(b'echo Hello, world\rexit\r')
output = stdout.read()
client.close()

sys.stdout.buffer.write(output)