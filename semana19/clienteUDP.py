import socket
HOST = '127.0.0.1'
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = input('Para sair use CTRL+X\n')
while msg != '\x18':
    udp.sendto(msg.encode(), dest)
    msg = input()
udp.close()
