#!/usr/bin/env python3
from random import randint
import time
import socket


serverAddressPort = ("192.168.1.33", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    sy=randint(1,100)

    sy=str(sy)
    bytesToSend2 = str.encode(sy)


