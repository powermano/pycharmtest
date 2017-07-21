from  socket import *

HOST = 'localhost'
PORT = 12345
Buffer = 1024
addr = (HOST,PORT)

tcpclisock = socket(AF_INET, SOCK_STREAM)
tcpclisock.connect(addr)

while True:
    data = input('input number :')
    if not data:
        break
    tcpclisock.send(data.encode(encoding='utf-8'))
    data = tcpclisock.recv(Buffer)
    if not data:
        break
    print(data.decode('utf-8'))


