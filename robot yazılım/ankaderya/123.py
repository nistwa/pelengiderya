import os 
from socket import *
host = 10.1.2.183
port = 13000
buf = 1024
addr = (10.1.2.184,12345)
UPDSock = from socket import (AF_INET, SOCK_DGRAM)
UPDSock.bind(addr)
print
"Waiting to receive messages..."
while True: 
    (data,addr) = UPDSock.recvform(buf)
    print
    "received message: " + data
    if data == "exit":
        break
UPDSock.close()
os.exit(0)