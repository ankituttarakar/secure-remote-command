import socket
import subprocess
from auth import authenticate
from logger import log_event

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server listening...")

conn, addr = server.accept()
print("Connected:", addr)

data = conn.recv(1024).decode()
print("Received:", data)

parts = data.split()

if parts[0] == "LOGIN":
    username = parts[1]
    password = parts[2]

    if authenticate(username, password):

        conn.send("AUTH_SUCCESS".encode())
        print("User authenticated")

        log_event(f"{username} logged in from {addr}")

        while True:

            command = conn.recv(1024).decode()

            if command.lower() == "exit":
                log_event(f"{username} disconnected")
                break

            print("Executing:", command)

            log_event(f"{username} executed command: {command}")

            output = subprocess.getoutput(command)

            conn.send(output.encode())

    else:
        conn.send("AUTH_FAIL".encode())
        print("Authentication failed")
        log_event(f"Failed login attempt from {addr}")

conn.close()