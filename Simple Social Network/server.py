import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
server_socket.bind(server_address)

# پذیرش اتصالات و انتظار برای اتصال کلاینت
server_socket.listen()
print('Waiting for a connection...')

# برای هر کلاینت جدید، یک ترد جدید ایجاد می کنیم
def handle_client(client_socket):
    client_socket.send('Welcome to the chatroom!'.encode())
    while True:
        # دریافت پیام از کلاینت
        message = client_socket.recv(1024).decode()
        if message:
            # نمایش پیام ارسال شده توسط کلاینت برای سایر کلاینت ها
            print(f"Client {client_socket.getsockname()} says: {message}")
            # ارسال پیام به همه کلاینت های دیگر
            for client in clients:
                if client != client_socket:
                    client.send(message.encode())

# لیستی برای ذخیره تمام کلاینت های متصل شده به سرور
clients = []

while True:
    # پذیرش اتصال کلاینت جدید
    client_socket, client_address = server_socket.accept()
    print(f"Connected by {client_address}")
    # اضافه کردن کلاینت جدید به لیست کلاینت ها
    clients.append(client_socket)
    # ایجاد یک ترد جدید برای هر کلاینت جدید
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

server_socket.close()
