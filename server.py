import socket

HOST = "127.0.0.1"
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"TCP Server läuft auf {HOST}:{PORT}")

conn, addr = server.accept()
print("Client verbunden:", addr)

with conn:
    conn.sendall(b"Willkommen vom Python TCP Server\n")

    while True:
        data = conn.recv(1024)

        if not data:
            break

        text = data.decode("utf-8").strip()
        print("Nachricht:", text)

        if text == "quit":
            conn.sendall(b"bye\n")
            break

        response = f"Echo: {text}\n"
        conn.sendall(response.encode("utf-8"))

server.close()
