# server.py
import socket
import os

# Constants
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 5001
SHARED_FOLDER = 'shared'

# Setup
server_socket = socket.socket()
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"[SERVER] Listening on {HOST}:{PORT}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"[SERVER] Connected to {addr}")

    filename = client_socket.recv(1024).decode()
    filepath = os.path.join(SHARED_FOLDER, filename)

    if os.path.isfile(filepath):
        client_socket.send(b'FOUND')
        with open(filepath, 'rb') as f:
            while chunk := f.read(1024):
                client_socket.send(chunk)
        print(f"[SERVER] File '{filename}' sent successfully.")
    else:
        client_socket.send(b'NOTFOUND')
        print(f"[SERVER] File '{filename}' not found.")

    client_socket.close()
