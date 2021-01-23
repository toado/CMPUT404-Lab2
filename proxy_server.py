import socket, os
from multiprocessing import Process  # For threading purposes

HOST = ""
PORT = 8001
PROXY_HOST = "www.google.com"
PROXY_PORT = 80
BUFFERSIZE = 1024

def handle_connection(client_conn, client_addr):
  # Receiving incoming data from client 
  # - Then forwarding that to google 
  # - Take the response from google & send it back to the client
  print("PID = {}".format(os.getpid()))
  with client_conn:
    client_data = client_conn.recv(BUFFERSIZE)
    print("Data received from client:\n\t{}".format(client_data))

    # Proxy server socket to connect to google.com
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy:
      proxy.connect((PROXY_HOST, PROXY_PORT))

      # Forward client data (its payload) to google
      print("THIS IS CLIENT DATA", client_data)
      proxy.sendall(client_data)

      # With google's response, send it back to the client
      proxy_data = proxy.recv(BUFFERSIZE)
      print("Data returned from Google:\n\t{}\n\n".format(proxy_data))
      client_conn.sendall(proxy_data)


def main():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Set socket w/ option SO_REUSEADDR to reuse the local socket within a TIME_WAIT state (don't have to wait for timeout to expire)
    # Bind (associate) the socket to its local address so clients can connect
    # and listen to requests
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print("Server socket is up and listening . . .")

    # Continue to listen for connection requests and accept them until forcefully closed
    while True:
      client_conn, client_addr = server.accept()
      print("Accepted a connection, connected by: {}".format(client_addr))

      p = Process(target=handle_connection, args=(client_conn, client_addr), daemon=True)
      p.start()
      client_conn.close()

if __name__ == "__main__":
  main()
