# client.py
import socket
import os

# Constants
SERVER_IP = '127.0.0.1'  # Change to actual server IP in real use
PORT = 5001
SAVE_FOLDER = 'downloads'

filename = input("Enter the filename to download: ")

client_socket = socket.socket()
client_socket.connect((SERVER_IP, PORT))
client_socket.send(filename.encode())

status = client_socket.recv(1024).decode()

if status == 'FOUND':
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    with open(f"{SAVE_FOLDER}/{filename}", 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)
    print(f"[CLIENT] File '{filename}' downloaded successfully.")
else:
    print(f"[CLIENT] File '{filename}' not found on server.")

client_socket.close()
