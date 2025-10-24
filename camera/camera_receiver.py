import cv2
import socket
import numpy as np

# UDP soketi oluştur
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sunucu IP ve port
ip = "192.168.1.33"
port = 6666

# Soketi belirtilen IP ve porta bağla
s.bind((ip, port))

print(f"Server is listening on {ip}:{port}")

while True:
    # Gelen veri ve istemci adresini al
    data, addr = s.recvfrom(1000000)

    try:
        # Gelen veriyi çöz ve görüntüyü oluştur
        img_array = np.frombuffer(data, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # Görüntüyü ekranda göster
        cv2.imshow('Camera Feed', img)
    except Exception as e:
        print(f"Error decoding image: {e}")
        continue

    # Çıkış için 'Esc' tuşuna bas
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Pencereleri kapat ve soketi kapat
cv2.destroyAllWindows()
s.close()
