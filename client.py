# Code Template Sourced from https://docs.python.org/3/library/socket.html#socket.socket.recv
import socket

# Constants
HOST = "www.google.com"
PORT = 80
PAYLOAD = f"GET / HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
BUFFERSIZE = 1024

def main():
    # Create a TCP/IP socket to connect to the remote socket
    # - Then send data (byte obj) to that remote socket
    # - Print the data received (byte object)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print("IP?? {}".format(socket.gethostbyname(HOST)))
        sock.connect((socket.gethostbyname(HOST), PORT))
        sock.sendall(PAYLOAD.encode())
        data = sock.recv(BUFFERSIZE)
    
        print("Data received:\n{}".format(data))

if __name__ == "__main__":
    main()
    