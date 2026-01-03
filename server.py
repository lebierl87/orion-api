from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class OrionHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(b'Orión está listo en Railway 🚀')

PORT = int(os.environ.get("PORT", 8000))
server = HTTPServer(('', PORT), OrionHandler)
server.serve_forever()
