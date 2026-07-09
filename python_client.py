import socket

HOST = "127.0.0.1"
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    print(sock.recv(1024).decode(), end="")

    while True:
        text = input("> ")

        sock.sendall((text + "\n").encode())

        response = sock.recv(1024).decode()
        print("<", response, end="")

        if text == "quit":
            break
