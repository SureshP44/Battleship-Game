"""
Developer : Suresh Perumal
Functionality: Contains the server code, which will setup the server, with twisted 
"""

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Server(DatagramProtocol):
    def __init__(self):
        self.clients = set()

    def datagramReceived(self, datagram, addr):
        #if the datagram is received from the user, end it will add the port into clients set to maintain list,
        datagram = datagram.decode('utf-8')
        if datagram == "ready":
            msg  = "\n".join([str(x) for x in self.clients])
            self.transport.write(msg.encode('utf-8'), addr)
            self.clients.add(addr)
            


if __name__ == '__main__':
    reactor.listenUDP(9999, Server())
    reactor.run()