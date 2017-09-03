##socket 嵌套字的网络编程
# from socket import *
#
# HOST = 'localhost'
# PORT = 12345
# Buffer = 1024
# addr = (HOST,PORT)
#
# tcpclisock = socket(AF_INET, SOCK_STREAM)
# tcpclisock.connect(addr)
#
# while True:
#     data = input('input number :')
#     if not data:
#         break
#     tcpclisock.send(data.encode(encoding='utf-8'))
#     data = tcpclisock.recv(Buffer)
#     if not data:
#         break
#     print(data.decode('utf-8'))

from twisted.internet import protocol, reactor

HOST='localhost'
PORT=21567

class TSClientProtocol(protocol.Protocol):
    def sendData(self):
        data = input('input text:')
        if data:
            print('...sending %s...' %data)
            self.transport.write(data.encode())
        else:
            self.transport.loseConnection()
    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data.decode())
        self.sendData()

class TSClientFactory(protocol.ClientFactory):
    protocol = TSClientProtocol
    clientConnectionlost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClientFactory())
reactor.run()





