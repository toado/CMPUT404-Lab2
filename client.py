import socket

HOST = "www.google.com"
PORT = 80
PAYLOAD = f"GET / HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
BUFFERSIZE = 1024

def main():
    # create a TCP/IP socket to connect to the remote socket
    # - then send data (byte obj) to that remote socket
    # - print the data received (byte object)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print("IP?? {}".format(socket.gethostbyname(HOST)))
        sock.connect((socket.gethostbyname(HOST), PORT))
        sock.sendall(PAYLOAD.encode(encoding='UTF-8'))
        data = sock.recv(1024)
    
    print("Data received:\n{}".format(data))

if __name__ == "__main__":
    main()
    