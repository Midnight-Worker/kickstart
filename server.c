#include <stdio.h>
#include <string.h>
#include <winsock2.h>

#pragma comment(lib, "ws2_32.lib")

#define PORT 9000
#define BUFFER_SIZE 1024

int main(void) {
    WSADATA wsa;
    SOCKET server_socket;
    SOCKET client_socket;
    struct sockaddr_in server_addr;
    struct sockaddr_in client_addr;
    int client_len = sizeof(client_addr);
    char buffer[BUFFER_SIZE];

    WSAStartup(MAKEWORD(2, 2), &wsa);

    server_socket = socket(AF_INET, SOCK_STREAM, 0);

    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr));
    listen(server_socket, 1);

    printf("C TCP Server läuft auf Port %d\n", PORT);

    client_socket = accept(
        server_socket,
        (struct sockaddr *)&client_addr,
        &client_len
    );

    printf("Client verbunden\n");

    send(client_socket, "Willkommen vom C TCP Server\n", 29, 0);

    while (1) {
        int bytes = recv(client_socket, buffer, BUFFER_SIZE - 1, 0);

        if (bytes <= 0) {
            break;
        }

        buffer[bytes] = '\0';

        printf("Nachricht: %s", buffer);

        if (strncmp(buffer, "quit", 4) == 0) {
            send(client_socket, "bye\n", 4, 0);
            break;
        }

        send(client_socket, "Echo: ", 6, 0);
        send(client_socket, buffer, bytes, 0);
    }

    closesocket(client_socket);
    closesocket(server_socket);
    WSACleanup();

    return 0;
}
