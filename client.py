import socket
import sys

try:
    # AF_INET     -> ipv4 address family
    # SOCK_STREAM -> TCP protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Created a socket for connect to the server
    print(" <o> - socket successfully created ! ")
except socket.error as err:
    print(" <x> - socket creation failed with error %s" %(err))

# PORT for the socket
port = 80 

try:
    # get the ip address of the host by name
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    print (" <x> - There was an error resolving the host")
    sys.exit()

# connect to the host with the host ip and the port name
s.connect(('127.0.0.1', port))
print (s.recv(1024).decode())

s.close()