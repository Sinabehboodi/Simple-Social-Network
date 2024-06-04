import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host , port))
s.listen()
while True :
    conn , addr = s.accept()
    print("get connection from ", addr)
    msg = "accepted"
    conn.send(msg.encode("utf_8"))
conn.close()

import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
msg = s.recv(1024)
print(msg)






