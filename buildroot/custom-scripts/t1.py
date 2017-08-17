import SimpleHTTPServer
import SocketServer
import os.path
import sys

handler = http.server.SimpleHTTPRequestHandler

class my_handler(handler):
    def do_GET(self):
        self.path = '/index.html'
        return Shandler.do_get(self)

if __name__ == "__main__":
    server = socketserver.TCPServer(('0.0.0.0', 8081), my_handler)
    server.serve_forever()
