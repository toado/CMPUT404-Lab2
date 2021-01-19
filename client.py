import socket, sys

HOST = "www.google.com"
PORT = 80   # Default port with TCP for an HTTP server
PAYLOAD = 'GET / HTTP/1.0\r\nHOST: {host}\r\n\r\n'
BUFFER_SIZE = 4096

# Creating a client socket (the endpoint of a conversation)
def create_TCP_socket():
    print("\nAttempting to create socket . . .")
    try:
        # AF_INET refers to IPV4
        # SOCK_STREAM refers to TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Successfully created socket\n")
        return sock

    except OSError:
        print("Failed to create socket: Error: {}\n".format(OSError))
        sys.exit()

# Get host IP
def get_remote_ip():
    print(f'Attempting to get IP for {HOST} . . .')
    try:
        remote_ip = socket.gethostbyname(HOST)

    except socket.gaierror:
        print("Hostname could be resolved. Exiting ...\n")
        sys.exit()
    
    print("Successfully connected to {}\n".format(HOST))
    return remote_ip

# Send data to server
def send_data(sock, payload):
    print("Sending payload . . .")
    try:
        sock.sendall(payload.encode())

    except socket.error:
        print("Send failed\n")

    print("Payload successfully sent!\n")

def main():
    try:
        # Try creating the socket and getting HOST IP then connecting
        sock = create_TCP_socket()    
        remote_ip = get_remote_ip()
        sock.connect((remote_ip, PORT))
        print("Socket connected to {} on IP: {}".format(HOST, remote_ip))

        # Send data & shutdown
        send_data(sock, PAYLOAD)
        sock.shutdown(socket.SHUT_WR)

        # Continue to accept all data until none left
        full_data = b""
        while True:
            data = sock.recv(BUFFER_SIZE)
            
            if not data:
                break
            
            full_data += data
        
        print(full_data)

    except Exception as e:
        print(e)

    # Always close the socket at the end!
    finally:
        sock.close()

if __name__ == "__main__":
    main()
