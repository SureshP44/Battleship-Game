"""
Developer : Suresh Perumal
Functionality: Contains the Client of the P2P network  using the twisted package in python
"""
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

class Client(DatagramProtocol):
    def __init__(self, host, port):
        # initialize the host and address.
        if host == 'localhost':
            host = "127.0.0.1"
        self.id = host, port
        self.address = None
        self.server = 'localhost', 9999
        print("working on :",self.id)

    def startProtocol(self):
        #startProtocol will start the conversation with server by sending ready, and it is encrypted and sent to server
        self.transport.write("ready".encode("utf-8"), self.server)
    
    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode('utf-8')
        if addr == self.address:
            print("Choose a client", datagram)
            self.address = input('write host'), input('write port')
            reactor.callInThread()


        print(addr, ":", datagram)
    
    def send_message(self):
         #sending messages, in a encrypted form to server
        while True:
            self.transport.write(input(":::").encode('utf-8'), self.address)

if __name__ == '__main__':
    port = randint(1000, 5000)
    reactor.listenUDP(port, Client('localhost', port))
    reactor.run()