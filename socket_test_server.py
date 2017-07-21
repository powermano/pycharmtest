from socket import *
from time import ctime

HOST = ''
PORT = 12345
Buffer = 1024
addr = (HOST,PORT)

tcpsersock = socket(AF_INET, SOCK_STREAM)
tcpsersock.bind(addr)
tcpsersock.listen(5)

while True:
    print('waiting for connection')
    tcpclisock, addr = tcpsersock.accept()
    print('...connection from :', addr)

    while True:
        data = tcpclisock.recv(Buffer)
        if not data:
            break
        tcpclisock.send('[%s] %s'.encode(encoding='utf-8') %(bytes(ctime(), 'utf-8'), data))




