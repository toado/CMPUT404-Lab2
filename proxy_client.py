import socket
from multiprocessing import Pool

# Constants
HOST = "localhost"
PORT = 8001
BUFFERSIZE = 1024
PAYLOAD = f"GET / HTTP/1.1\r\nHost: {HOST}\r\n\r\n" 

# Create a TCP/IP socket to connect to the remote socket
# - Then send data (byte obj) to that remote socket
# - Then print the data received (byte object)
def create_and_connect(address):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(address)
    sock.sendall(PAYLOAD.encode())

    data = sock.recv(BUFFERSIZE)
    print("Data received:\n\t{}".format(repr(data)))

# To test threading; code below shown from Monday's lab
def main():
  address = [(HOST, PORT)]
  with Pool() as p:
    p.map(create_and_connect, address*5)

if __name__ == "__main__":
  main()
  # create_and_connect((HOST, PORT))
