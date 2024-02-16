import socket
import select
import sys

def main():
    # Prompt the user for host and port
    host = input("Enter host name: ")
    port = int(input("Enter port: "))

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to the server
        try:
            sock.connect((host, port))
        except ConnectionError as e:
            print(f"Failed to connect to {host}:{port}")
            return
        
        print(f"Connected to {host}:{port}. You can start sending messages.")
        
        # Keep the connection open, and listen for data to read or write
        while True:
            # Use select to wait for input from stdin or the socket
            read_sockets, _, _ = select.select([sys.stdin, sock], [], [])
            
            for read_socket in read_sockets:
                if read_socket == sock:
                    # Incoming message from remote server
                    data = sock.recv(4096)
                    if not data:
                        print("\nDisconnected from server.")
                        return
                    else:
                        # Print data, using 'replace' to handle undecodable bytes
                        print(data.decode('utf-8', 'replace'), end='')
                else:
                    # User entered a message
                    msg = sys.stdin.readline()
                    sock.sendall(msg.encode())
                    # Optional: Print it to the screen or handle accordingly
                    # print(f"You: {msg}", end='')

if __name__ == "__main__":
    main()

