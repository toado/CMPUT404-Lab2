# Code Template Sourced from https://docs.python.org/3/library/socket.html#socket.socket.recv
import socket

HOST = ""   # Symbolic name meaning all available interfaces
PORT = 8001 
BUFFERSIZE = 1024

def main():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Set socket w/ option SO_REUSEADDR to reuse the local socket within a TIME_WAIT state (don't have to wait for timeout to expire)
    # Bind (associate) the socket to its local address so clients can connect
    # and listen to requests
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    
    # Continue to listen for requests and accept them until forcefully closed
    while True:
      conn, addr = server.accept()
      print("Connection information: {}".format(conn))
      print(f'Connected by: {addr}')

      # Receive the incoming data and send it back to the client
      with conn:
        data = conn.recv(BUFFERSIZE)
        print("Data received: {}\n".format(data))

        conn.sendall(data)
  
if __name__ == "__main__":
  main()