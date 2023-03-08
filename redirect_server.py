import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler

class UnixSocketHttpServer(socketserver.UnixStreamServer):
    def get_request(self):
        request, client_address = super(UnixSocketHttpServer, self).get_request()
        return (request, ["local", 0])

server = UnixSocketHttpServer(("/var/lib/waziapp/proxy.sock"), Handler)

server.serve_forever()