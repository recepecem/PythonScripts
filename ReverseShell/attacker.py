import socket
host = "0.0.0.0"
port = 1236
soket = socket.socket()
soket.bind((host, port))
soket.listen()
conn, addr = soket.accept()
print("Connection Established [",str(conn),"]")
mesaj = "Connection Established".encode()
conn.send(mesaj)
while True:
    command = input("command: ")
    conn.send(command.encode())
    if komut.lower() == "exit":
        break
    result = conn.recv(1024).decode()
    print(result)
conn.close()
soket.close()
