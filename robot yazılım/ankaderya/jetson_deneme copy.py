#/usr/bin/env python3
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import serial #arduino ile seri haberleşme için gerekli kütüphane
import pygame#joystickten veri almak için gerekli kütüphane
import serial.tools.list_ports as port_list#portları listelemek için gerekli kütüphane
import time
#burda usb portları listeliyoruz
ports = list(port_list.comports())
for p in ports:
    print (p)

#seri haberleşmeyi com4 portu üzerinden 115200 baude rate oranında başlatıyoruz. bu sayı arduino ile aynı olmalı
#ser=serial.Serial('com4',115200,timeout=1)

#joysticki başlat
pygame.init()
joystick=pygame.joystick.Joystick(0)
joystick.init()
print(f"Extreme 3D Pro bulundu:{joystick.get_name()}")

while True:
    #joystickten gelen verileri güncelliyoruz
    pygame.event.pump()
    #burda ileri geri gaz verilerini 1 ile -1 arasından 1000 ile 2000 arasına çevirme işlemini yapıyoruz
    #sonda ki ig karakterlerini aldığında arduino çalışıyor. bu veriler bize hangi yönde gönderdiğimiz için gerekli

    SagSol=int(90-(joystick.get_axis(0)*90))
    #sagSol=str(int(180-(joystick.get_axis(0)*90)))+'ss'
    #print(ileriGeri,sagSol)
    
    if SagSol>170:
        SagSol=165
    if SagSol<10:
        SagSol=15
    print(SagSol)

    kit.servo[0].angle=SagSol

    #hespladığımız verileri arduinoya gönderiyoruz
    #ser.write(sagSol.encode('utf-8'))
    #ser.flush()
    #ser.write(ileriGeri.encode('utf-8'))
    #ser.flush()
    #time.sleep(0.1)

#0-90 = geri
#90-180 = ileri+