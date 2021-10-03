import socket
import datetime

s = socket.socket()

print ("Socket successfully created")

port = 12345

s.bind(('', port))

print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)
print ("socket is listening")

now = datetime.datetime.now()
while True:

    # Establish connection with client.
    c, addr = s.accept()
    print ('Got connection from', addr )

    # Send Time and Date to Client
    c.send(str(now).encode())

    # Close the connection with the client
    c.close()

# Breaking once connection closed
    break
