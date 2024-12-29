import socket
from random import randint
import pygame#joystickten veri almak için gerekli kütüphane
import serial.tools.list_ports as port_list#portları listelemek için gerekli kütüphane
import time
ports = list(port_list.comports())
for p in ports:
    print (p)
pygame.init()
joystick=pygame.joystick.Joystick(0)
joystick.init()
print(f"Extreme 3D Pro bulundu:{joystick.get_name()}")
serverAddressPort = ("10.1.1.109", 20001)

bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    try:
        pygame.event.pump()
        cw = int(90 - (joystick.get_axis(1) * 90))
        ccw = int(90 + (joystick.get_axis(1) * 90))
        cw = int(90 - (joystick.get_axis(0) * 90))
        ccw = int(90 + (joystick.get_axis(0) * 90))
        if cw > 170:
            cw = 165
        if cw < 10:
            cw = 15
        print(cw)

        if ccw > 170:
            ccw = 165
        if ccw < 10:
            ccw = 15
        #print(ccw)
        # Send to server using created UDP socket
        sy=randint(1,100)
        msgFromClient = str(cw)
        #msgFromClient2 = str(ccw)

        bytesToSend = str.encode(msgFromClient)
        #bytesToSend2 = str.encode(msgFromClient2)

        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        #UDPClientSocket.sendto(bytesToSend2, serverAddressPort)
    except socket.error as msg:
        print(msg)

"""
msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)
"""

