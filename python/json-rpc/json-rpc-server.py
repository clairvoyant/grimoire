#!/usr/bin/python


from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import threading
import argparse
import re
import cgi
import json


# TODO routing of URLs.
 
class LocalData(object):
    records = {}
 
class HTTPRequestHandler(BaseHTTPRequestHandler):
    """ HTTPRequestHandler implements POST and GET. to add and remove records"""
 
    def do_POST(self):
        if None != re.search('/api/v1/addrecord/*', self.path):
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'application/json':
                length = int(self.headers.getheader('content-length'))
                data = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
                recordID = self.path.split('/')[-1]
                LocalData.records[recordID] = data
                print "record %s is added successfully" % recordID
            else:
                data = {}
 
            self.send_response(200)
            self.end_headers()
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
 
        return
 
    def do_GET(self):
        if None != re.search('/api/v1/getrecord/*', self.path):
            recordID = self.path.split('/')[-1]
            if LocalData.records.has_key(recordID):
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(LocalData.records[recordID])
            else:
                self.send_response(400, 'Bad Request: record does not exist')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
        elif None != re.search('/api/v1/listrecord', self.path):
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                serial = json.dumps(LocalData.records.keys())
                self.wfile.write(serial)
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
 
        return
 
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    allow_reuse_address = True
 
    def shutdown(self):
        self.socket.close()
        HTTPServer.shutdown(self)
 
class SimpleHttpServer():
    def __init__(self, ip, port):
        self.server = ThreadedHTTPServer((ip,port), HTTPRequestHandler)
 
    def start(self):
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
 
    def waitForThread(self):
        self.server_thread.join()
 
    def addRecord(self, recordID, jsonEncodedRecord):
        LocalData.records[recordID] = jsonEncodedRecord
 
    def stop(self):
        self.server.shutdown()
        self.waitForThread()
 
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='JSON-RPC Server')
    parser.add_argument('address',           help='Server address ')
    parser.add_argument('port',    type=int, help='TCP port')
    args = parser.parse_args()

    LocalData.records["one"]   = { "one": 1 }
    LocalData.records["two"]   = { "two": 1 }
    LocalData.records["three"] = { "three": 3}
 
    server = SimpleHttpServer(args.address, args.port)
    print 'JSON-RPC Server started...........'
    server.start()
    server.waitForThread()
