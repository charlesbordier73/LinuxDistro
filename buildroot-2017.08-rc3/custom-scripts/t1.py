import SimpleHTTPServer
import SocketServer
import os.path
import sys

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = '/index.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler

server = SocketServer.TCPServer(('0.0.0.0', 8082), Handler)
server.serve_forever()
