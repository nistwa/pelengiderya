#!/usr/bin/env python3
import cv2
import numpy as np
import socket

# Kamera bağlantısını başlat
cap = cv2.VideoCapture(0)  # Varsayılan kamera için 0

# Bağlanacağınız bilgisayarın IP adresi ve port numarası
receiver_ip = "10.1.2.159"
receiver_port = 12345

# UDP soketini oluştur
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Maksimum UDP paket boyutu
MAX_UDP_PACKET_SIZE = 65507

while True:
    ret, frame = cap.read()  # Kameradan bir kare al
    if not ret:
        print("Kamera görüntüsü alınamadı.")
        break

    # Kareyi işleyerek gönderilebilir formata dönüştür (örneğin, JPEG)
    _, img_encoded = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 50])  # Sıkıştırma kalitesini %50 yap
    data = np.array(img_encoded)
    string_data = data.tobytes()  # tostring yerine tobytes kullan

    # Veri paketini parçala ve gönder
    if len(string_data) > MAX_UDP_PACKET_SIZE:
        print("Gönderilen veri çok büyük, parçalanıyor...")
        for i in range(0, len(string_data), MAX_UDP_PACKET_SIZE):
            sock.sendto(string_data[i:i + MAX_UDP_PACKET_SIZE], (receiver_ip, receiver_port))
    else:
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
