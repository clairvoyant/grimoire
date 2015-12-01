#!/usr/bin/env python


#
# simple example # of a quick 
# server with and API # for real things
# its better to use 
# django+pinax.You will get for free
#    auth
#    url encoding
#    database
#    get vs post
#

#
#


from twisted.web import server, resource
from twisted.internet import reactor, endpoints

object_example = { "menu": {
  "id": "%s",
  "value": "name",
  "related": {
    "item": [
      {"var1": "val1"},
      {"var2": "val2"},
      {"var3": "val3"}
    ]
  }
}}

class Counter(resource.Resource):
    isLeaf = True
    numberRequests = 0

    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "application/json")
        return str(object_example) 

endpoints.serverFromString(reactor, "tcp:8080").listen(server.Site(Counter()))
reactor.run()
