#include <iostream>
#include <cstring>
#include <arpa/inet.h>
#include <unistd.h>
#include <sys/socket.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <host> <port>" << std::endl;
        return 1;
    }

    const char* server_name = argv[1];
    const int server_port = std::stoi(argv[2]);

    struct sockaddr_in server_address;
    memset(&server_address, 0, sizeof(server_address));
    server_address.sin_family = AF_INET;
    inet_pton(AF_INET, server_name, &server_address.sin_addr);
    server_address.sin_port = htons(server_port);

    int sock;
    if ((sock = socket(PF_INET, SOCK_STREAM, 0)) < 0) {
        std::cerr << "Could not create socket" << std::endl;
        return 1;
    }

    if (connect(sock, (struct sockaddr*)&server_address, sizeof(server_address)) < 0) {
        std::cerr << "Could not connect to server" << std::endl;
        return 1;
    }

    std::cout << "Connected to " << server_name << " on port " << server_port << std::endl;

    // Communication loop
    char buffer[4096];
    while (true) {
        std::cout << "> ";
        std::string input;
        std::getline(std::cin, input);

        if (input == "exit") {
            break;
        }

        send(sock, input.c_str(), input.length(), 0);

        // Receive response
        int len = recv(sock, buffer, sizeof(buffer) - 1, 0);
        if (len < 0) {
            std::cerr << "Failed to receive data." << std::endl;
            break;
        }

        buffer[len] = '\0';
        std::cout << "Server: " << buffer << std::endl;
    }

    close(sock);
    return 0;
}

