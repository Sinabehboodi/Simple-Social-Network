import socket
import threading
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
client_socket.connect(server_address)

def receive_messages():
    while True:
        message = client_socket.recv(1024).decode()
        if message:
            print(message)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input()
    client_socket.send(message.encode())