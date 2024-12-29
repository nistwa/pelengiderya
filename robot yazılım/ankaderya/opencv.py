#!/usr/bin/env python3
import cv2
import numpy as np
import socket

# Kamera bağlantısını başlat
cap = cv2.VideoCapture(0)  # 0 varsayılan kamerayı seçer, farklı bir kamera kullanıyorsanız uygun indeksi girin

# Bağlanacağınız bilgisayarın IP adresi ve port numarası
receiver_ip = "10.1.2.159"
receiver_port = 12345

# UDP soketini oluştur
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    ret, frame = cap.read()  # Kameradan bir kare al

    # Kareyi işleyerek gönderilebilir formata dönüştür (örneğin, JPEG)
    _, img_encoded = cv2.imencode('.jpg', frame)
    data = np.array(img_encoded)
    string_data = data.tostring()

    # Kareyi gönder
    sock.sendto(string_data, (receiver_ip, receiver_port))

    # Gönderilen kareyi ekranda göster
    cv2.imshow('Frame', frame)

    # Çıkış için 'q' tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Döngü sonlandığında kamera bağlantısını ve soketi kapat
cap.release()
sock.close()
cv2.destroyAllWindows()
