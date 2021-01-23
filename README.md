Question 1: How do you specify a TCP socket in Python?
- Using the parameter SOCK_STREAM when creating the socket

Question 2: What is the difference between a client socket and a server socket in Python?
- Server socket is created and binded to a port to listen for a incoming connections from client
- A client socket is created to connect to a server and send data then listens for a response

Question 3: How do we instruct the OS to let us reuse the same bind port?
- With the parameter socket.USE_RESUADDR in the function call to setsockopt()

Question 4: What information do we get about incoming connections?
- Get IP address and port connected to from the incoming connections as well as its connection information(local address, remote address, protocol, socket type)

Question 5: What is returned by recv() from the server after it is done sending the HTTP request?
- Returns the data as a byte-string

Question 6: Provide a link to your code on GitHub.
- https://github.com/toado/CMPUT404-Lab2

Info!

BSD Socket Interfaces
- Set of standard function calls that can be used in a an application that allows programmers to add Internet communications to their product (network protocols)
- Will be using the socket module to allow access to these interfaces 