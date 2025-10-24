#!/usr/bin/env python3
import socket
from adafruit_servokit import ServoKit

# Servo ve UDP Ayarları
kit = ServoKit(channels=16)
localIP = "10.1.1.109"
localPort = 20001
bufferSize = 1024

# Servo Limitleri
MIN_ANGLE = 10
MAX_ANGLE = 170

# UDP Sunucusu Başlatma
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

while True:
    try:
        # Mesaj Alımı
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0].decode("utf-8")
        print(f"Received message: {message}")

        # Mesaj İşleme
        cw = int(message)
        cw = max(MIN_ANGLE, min(MAX_ANGLE, cw))  # Açıları sınırlandır

        # Servo Motor Kontrolü
        kit.servo[0].angle = cw
        print(f"Servo angle set to {cw}")

    except ValueError:
        print("Invalid message received")
    except Exception as e:
        print(f"An error occurred: {e}")
