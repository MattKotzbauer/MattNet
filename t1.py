import socket
import threading

def handle_client(client_socket):
    while True:
        request = client_socket.recv(4096)
        if not request:
            break
        
        client_socket.send(request)

    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345)) # (localhost port 12345)
    server.listen(5)

    print("[*] Listening on port 12345")

    try:
        while True:
            client_socket, client_address = server.accept()
            print("[*] Accepted connection from: %s:%d" % (client_address[0], client_address[1]))

            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print("\n[*] Exiting...")

if __name__ == "__main__":
    main()

