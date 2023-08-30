import socket
import sys

try:
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Success")
except socket.error as socketError:
    print("Cannot create socket")

port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')

except socket.gaierror as gai:
    print("Could not resolve host name", gai)
    sys.exit()

s.connect((host_ip,port))

print("Connection Successful")