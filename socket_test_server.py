##socket 嵌套字的网络编程

# from socket import *
# from time import ctime
#
# HOST = ''
# PORT = 12345
# Buffer = 1024
# addr = (HOST,PORT)
#
# tcpsersock = socket(AF_INET, SOCK_STREAM)
# tcpsersock.bind(addr)
# tcpsersock.listen(5)
#
# while True:
#     print('waiting for connection')
#     tcpclisock, addr = tcpsersock.accept()
#     print('...connection from :', addr)
#
#     while True:
#         data = tcpclisock.recv(Buffer)
#         if not data:
#             break
#         tcpclisock.send('[%s] %s'.encode(encoding='utf-8') %(bytes(ctime(), 'utf-8'), data))


##twisted 框架的编程
from twisted.internet import protocol, reactor
from time import ctime

PORT=21567

class TSServerProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt= self.clnt= self.transport.getPeer().host
        print('...connection from:%s'%clnt)
    def dataReceived(self, data):
        self.transport.write('[%s] %s'.encode('utf-8') %(ctime().encode('utf-8'), data))

factory = protocol.Factory()
factory.protocol = TSServerProtocol
print('waiting for connection...')
reactor.listenTCP(PORT,factory)
reactor.run()






