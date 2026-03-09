import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Username: ")
password = input("Password: ")

msg = f"LOGIN {username} {password}"

client.send(msg.encode())

response = client.recv(1024).decode()

print("Server response:", response)

if response == "AUTH_SUCCESS":

    while True:

        command = input("Enter command: ")

        if command.lower() == "exit":
            client.send(command.encode())
            break

        client.send(command.encode())

        output = client.recv(4096).decode()

        print("Output:\n", output)

client.close()