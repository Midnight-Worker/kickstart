#include <stdio.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")

#define HOST "127.0.0.1"
#define PORT "9000"
#define BUFFER_SIZE 1024

int main(void) {
    WSADATA wsa;
    SOCKET sock;
    struct addrinfo hints;
    struct addrinfo *result = NULL;
    char buffer[BUFFER_SIZE];
    char input[BUFFER_SIZE];

    WSAStartup(MAKEWORD(2, 2), &wsa);

    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;

    if (getaddrinfo(HOST, PORT, &hints, &result) != 0) {
        printf("getaddrinfo fehlgeschlagen\n");
        WSACleanup();
        return 1;
    }

    sock = socket(result->ai_family, result->ai_socktype, result->ai_protocol);

    if (connect(sock, result->ai_addr, (int)result->ai_addrlen) == SOCKET_ERROR) {
        printf("Verbindung fehlgeschlagen\n");
        closesocket(sock);
        freeaddrinfo(result);
        WSACleanup();
        return 1;
    }

    freeaddrinfo(result);

    printf("Verbunden mit %s:%s\n", HOST, PORT);

    int bytes = recv(sock, buffer, BUFFER_SIZE - 1, 0);
    if (bytes > 0) {
        buffer[bytes] = '\0';
        printf("< %s", buffer);
    }

    while (1) {
        printf("> ");

        if (!fgets(input, BUFFER_SIZE, stdin)) {
            break;
        }

        send(sock, input, (int)strlen(input), 0);

        bytes = recv(sock, buffer, BUFFER_SIZE - 1, 0);

        if (bytes <= 0) {
            break;
        }

        buffer[bytes] = '\0';
        printf("< %s", buffer);

        if (strncmp(input, "quit", 4) == 0) {
            break;
        }
    }

    closesocket(sock);
    WSACleanup();

    return 0;
}
