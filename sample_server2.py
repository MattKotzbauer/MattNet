import socket
import subprocess
import ssl
import os

def handle_client_connection(client_socket):
    username = client_socket.recv(1024).strip()
    client_socket.sendall(b'Password: ')
    password = client_socket.recv(1024).strip()

    if username != b'admin' or password != b'secret':
        client_socket.sendall(b'Authentication failed.\n')
        client_socket.close()
        return
    
    client_socket.sendall(b'Authenticated successfully.\n')

    allowed_commands = ['ls', 'whoami', 'date']

    while True:
        try:
            data = client_socket.recv(1024).decode().strip()
            if not data:
                break

            if data.split()[0] not in allowed_commands:
                client_socket.sendall(b'Command not permitted.\n')
                continue

            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = proc.stdout.read() + proc.stderr.read()
            client_socket.send(stdout_value)
        except Exception as e:
            print(f"Connection closed: {e}")
            break

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    
    server_socket.bind(('0.0.0.0', 2323))
    server_socket.listen(5)
    print("Listening on port 2323...")

    while True:
        client_sock, address = server_socket.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")
        
        secure_sock = context.wrap_socket(client_sock, server_side=True)
        
        handle_client_connection(secure_sock)

if __name__ == '__main__':
    main()

