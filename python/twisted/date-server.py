#!/usr/bin/env python

from twisted.internet import protocol, reactor, endpoints
import datetime

class DateServer(protocol.Protocol):
    def dataReceived(self, data):
        d=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
        self.transport.write(d)

class DateServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return DateServer()

endpoints.serverFromString(reactor, "tcp:12345").listen(DateServerFactory())
reactor.run()
