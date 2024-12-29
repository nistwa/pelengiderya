import cv2
import socket
import pickle
import os
import numpy as np

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="192.168.1.33"
port=6666
s.bind((ip,port))

while True:
    x=s.recvfrom(1000000)
    client_ip=x[1][0]
    data=x[0]
    img=cv2.imdecode(data,cv2.IMREAD_COLOR)
    cv2.imshow('Img Server',img)
    if cv2.waitKey(5) & 0xFF ==27:
        break
cv2.destroyAllWindows()