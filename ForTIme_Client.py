import socket
s = socket.socket()
port = 12345
host_ip = socket.gethostname()
print(host_ip)
s.connect((host_ip, port))
print("the socket has successfully connected to the Server")
print ("The Date & Time recived from Server: ", s.recv(1024).decode())
s.close()