import socket
import pygame #joystickten veri almak için gerekli kütüphane
import serial.tools.list_ports as port_list #portları listelemek için gerekli kütüphane
ports = list(port_list.comports())
for p in ports:
    print (p)
pygame.init()
joystick=pygame.joystick.Joystick(0)
joystick.init()
print(f"Extreme 3D Pro bulundu:{joystick.get_name()}")
#serverAddressPort = ("10.1.1.109", 20001)
serverAddressPort = ("192.168.1.34", 20001)

bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    try:
        pygame.event.pump()
        cwig = int(90 - (joystick.get_axis(1) * 90))
        ccwig = int(90 + (joystick.get_axis(1) * 90))
        cwss = int(90 - (joystick.get_axis(0) * 90))
        ccwss = int(90 + (joystick.get_axis(0) * 90))
        if cwig > 170:
            cwig = 165
        if cwig < 10:
            cwig = 15
        buton0=joystick.get_button(2)
        print(cwig,cwss)

        if ccwig > 170:
            ccwig = 165
        if ccwig < 10:
            ccwig = 15
        #print(ccw)
        # Send to server using created UDP socket
        msgFromClient = str((cwig,cwss))
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