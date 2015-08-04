#!/usr/bin/env python
# 
#
# very simple example of a chat based
# on a line interface
# each line received will be broadcast
# to each client
#
#  Chat there will be one per subscriber
#



from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class Chat(LineReceiver):

    def __init__(self, addr, users):
        self.users     = users
        self.name      = str(addr)
        self.delimiter = "\n"

    def connectionMade(self):
        self.sendLine("<connected to M2M chat>")
        print "jrv:: adding [%s]"% (self.name)
        self.users[self.name] = self

    def connectionLost(self, reason):
        if self.users.has_key(self.name):
            del self.users[self.name]

    def lineReceived(self, line):
            self.handle_CHAT(line)

    def handle_CHAT(self, message):
        message = "<%s> %s" % (self.name, message)
        print "jrv::", message
        self.sendLine(message)
        for name, protocol in self.users.iteritems():
            if ':' in message:
                self.exc(message.split(':')[0])
            if protocol != self:
                protocol.sendLine(message)

    def exc(self, cmd):
        print cmd
        if cmd == 'who':
            for i in self.users:
                print i


class ChatFactory(Factory):

    def __init__(self):
        self.users = {} # maps user names to Chat instances

    def buildProtocol(self, addr):
        print "jrv:: new protocol"
        return Chat(addr, self.users)


reactor.listenTCP(8821, ChatFactory())
reactor.run()
