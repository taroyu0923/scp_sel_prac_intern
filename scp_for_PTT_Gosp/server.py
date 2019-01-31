from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import requests

class WebServer(SimpleHTTPRequestHandler):

    def do_GET(self):
        print(self.headers)
        super().do_GET()

print('Press Ctrl+C to stop...')
TCPServer(('127.0.0.1', 8000), WebServer).serve_forever
