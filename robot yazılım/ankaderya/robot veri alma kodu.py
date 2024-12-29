#!/usr/bin/env python3
from ast import Delete
import socket
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
 

#localIP     = "10.1.2.103"#asfa ip
localIP     = "192.168.1.35"#ankaderya modem ip
localPort   = 20001

bufferSize  = 1024

 

#msgFromServer       = "Hello UDP Client"

#bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 
 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))
print("Hello World")
 

print("UDP server up and listening")

 

# Listen for incoming datagrams
def ileri():
    kit.servo[0].angle=10
    kit.servo[1].angle=10
    kit.servo[2].angle=135
    kit.servo[3].angle=135
    kit.servo[4].angle=0
    kit.servo[5].angle=0

def geri():
    kit.servo[0].angle=180
    kit.servo[1].angle=180
    kit.servo[2].angle=10
    kit.servo[3].angle=10
    kit.servo[4].angle=0
    kit.servo[5].angle=0

def sag():
    kit.servo[0].angle=10
    kit.servo[1].angle=180
    kit.servo[2].angle=180
    kit.servo[3].angle=10
    kit.servo[4].angle=0
    kit.servo[5].angle=0

def sol():
    kit.servo[0].angle=180
    kit.servo[1].angle=10
    kit.servo[2].angle=10
    kit.servo[3].angle=180
    kit.servo[4].angle=0
    kit.servo[5].angle=0
""""
def sol_don():
    kit.servo[2].angle=10
    kit.servo[3].angle=180
    kit.servo[0].angle=180
    kit.servo[1].angle=10
    kit.servo[4].angle=0
    kit.servo[5].angle=0

def sag_don():
    kit.servo[2].angle=180
    kit.servo[3].angle=10
    kit.servo[0].angle=10
    kit.servo[1].angle=180
    kit.servo[4].angle=0
    kit.servo[5].angle=0
"""
def dur():
    kit.servo[0].angle=90
    kit.servo[1].angle=90
    kit.servo[2].angle=90
    kit.servo[3].angle=90
    kit.servo[4].angle=90
    kit.servo[5].angle=90

def yukari():
    kit.servo[0].angle=0
    kit.servo[1].angle=0
    kit.servo[2].angle=0
    kit.servo[3].angle=0
    kit.servo[4].angle=180
    kit.servo[5].angle=180

def assagı():
    kit.servo[0].angle=0
    kit.servo[1].angle=0
    kit.servo[2].angle=0
    kit.servo[3].angle=0
    kit.servo[4].angle=10
    kit.servo[5].angle=10


while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    #message = int(bytesAddressPair[0].decode("utf-8"))
    message = bytesAddressPair[0].decode("utf-8")
    message=str(message)
    mtn=message.split(",")
    ilkVeri=int(mtn[0][1:])
    ikinciVeri=int(mtn[1][1:])
    ucuncuVeri=int(mtn[2][1:])
    dortuncuVeri=int(mtn[3][1:-1])
    print(ilkVeri,ikinciVeri,ucuncuVeri,dortuncuVeri)
    
    
    if ilkVeri > 130:
        ileri()
    elif ilkVeri < 65:
        geri()
    elif ikinciVeri < 65:
        sag()
    elif ikinciVeri < 130:
        sol()
    elif dortuncuVeri > 30:
        yukari()
    elif dortuncuVeri < 160:
        assagı()
    else:
        dur()


 #ASIL KOD  

