# import socket
# import os

# # Unix Domain socket path
# unix_socket_path = "/home/fx/proxy_test.sock"

# # Local port to forward the HTTP traffic to
# local_port = 9000

# # Create a Unix Domain socket to receive incoming HTTP requests
# if os.path.exists(unix_socket_path):
#     os.remove(unix_socket_path)

# unix_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
# unix_sock.bind(unix_socket_path)
# os.chmod(unix_socket_path, 0o777)
# unix_sock.listen(1)

# # Loop forever, accepting incoming HTTP requests and forwarding them to the local port
# while True:
#     # Wait for incoming HTTP request on Unix Domain socket
#     client, address = unix_sock.accept()
#     print(f"Received request from {address}")
    
#     # Forward the HTTP request to the local port
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as local_sock:
#         local_sock.connect(('127.0.0.1', local_port))
#         data = client.recv(1024)
#         while data:
#             local_sock.send(data)
#             data = client.recv(1024)

#         client.close()
#         local_sock.close()
    
#     # Log the HTTP request
#     print(data.decode())


# import socket
# import socketserver
# import threading

# class MyUnixStreamServer(socketserver.UnixStreamServer):
#     def handle_request(self, request, client_address):
#         s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
#         s.connect(('localhost', 9000)) 
        
#         data = request.recv(1024)
#         s.sendall(data)
#         response = s.recv(1024)
#         request.sendall(response)
        
#         s.close()
#         request.close()

# #server_address = '/var/lib/waziapp/proxy.sock'
# server_address = '/home/fx/proxy_test.sock'
# server = MyUnixStreamServer(server_address, None)
# tcp_server = socketserver.TCPServer(('localhost', 9000), MyUnixStreamServer)

# # Servers in separate threads
# unix_thread = threading.Thread(target=server.serve_forever)
# tcp_thread = threading.Thread(target=tcp_server.serve_forever)
# unix_thread.start()
# tcp_thread.start()


# import socket
# import socketserver

# from requests import request

# class UnixSocketHttpServer(socketserver.UnixStreamServer):
#     def get_request(self):
#         s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
#         s.connect(('localhost', 9000))  
        
#         data = request.recv(1024)
#         s.sendall(data)
#         response = s.recv(1024)
#         request.sendall(response)
        
#         s.close()
#         request.close()

# server_address = '/var/lib/waziapp/proxy.sock'
# server = UnixSocketHttpServer(server_address, None)

# server.serve_forever()



import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler

class UnixSocketHttpServer(socketserver.UnixStreamServer):
    def get_request(self):
        request, client_address = super(UnixSocketHttpServer, self).get_request()
        return (request, ["local", 0])

server = UnixSocketHttpServer(("/var/lib/waziapp/proxy.sock"), Handler)

server.serve_forever()