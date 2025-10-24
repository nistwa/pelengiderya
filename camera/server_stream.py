import cv2
import numpy as np
import socket

# Kamerayı başlat
cap = cv2.VideoCapture(0)  # Varsayılan kamera için 0, başka bir kamera için indeks numarası

# Alıcı bilgisayarın IP adresi ve port numarası
receiver_ip = "127.0.0.1"  # Alıcı bilgisayarın IP adresi
receiver_port = 12345  # Port numarası

# UDP soketini oluştur
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    ret, frame = cap.read()  # Kameradan bir kare al

    if not ret:
        break

    # Kareyi JPEG formatında kodlayın
    _, img_encoded = cv2.imencode('.jpg', frame)
    data = img_encoded.tobytes()  # Baytlara dönüştür

    # Veriyi gönder
    sock.sendto(data, (receiver_ip, receiver_port))

    # Gönderilen kareyi göster
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
sock.close()
cv2.destroyAllWindows()
