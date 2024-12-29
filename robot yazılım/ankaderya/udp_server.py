#!/usr/bin/env python3
import socket
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

localIP = "192.168.1.33"

localPort = 20001

bufferSize = 1024

# msgFromServer       = "Hello UDP Client"

# bytesToSend         = str.encode(msgFromServer)


# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams

while (True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = int(bytesAddressPair[0].decode("utf-8"))
    cw = int(90 - (message * 90))
    ccw = int(90 + (message * 90))
    # address = bytesAddressPair[1]
    if cw > 170:
        cw = 165
    if cw < 10:
        cw = 15
    print(cw)

    if ccw > 170:
        ccw = 165
    if ccw < 10:
        ccw = 15
    print(ccw)

    kit.servo[0].angle = cw
    kit.servo[1].angle = ccw
    kit.servo[2].angle = cw
    kit.servo[3].angle = ccw
    kit.servo[4].angle = cw
    kit.servo[5].angle = ccw

    # Sending a reply to client

    # UDPServerSocket.sendto(bytesToSend, address)

