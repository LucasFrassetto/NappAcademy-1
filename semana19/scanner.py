'''
Port-scanner.py
Código adaptado do livro
"Python para Pentest" - ISBN 788575 226926
página 64
'''
import socket
host = '127.0.0.1'
portas = [21, 23, 80, 3306]
# portas = list(range(0,65536))
for porta in portas:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    codigo_retorno = sock.connect_ex((host, porta))
    sock.close()
    if codigo_retorno == 0:
        print(porta)
