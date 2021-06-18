import socket
HOST = '127.0.0.1'
PORT = 5001
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
msg = input('Para sair use CTRL+X\n')
while msg != '\x18':
    tcp.send(msg.encode())
    msg = input()
tcp.close()
