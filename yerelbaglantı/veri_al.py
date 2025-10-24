#!/usr/bin/env python3
import socket

localIP = "192.168.1.33"
localPort = 20001

bufferSize = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("Hello World")

print("UDP server up and listening")

while (True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    # message = int(bytesAddressPair[0].decode("utf-8"))
    message = bytesAddressPair[0].decode("utf-8")
    message = str(message)
    print(message)