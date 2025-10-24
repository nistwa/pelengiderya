import cv2
import socket
import pickle

# UDP soketi oluştur
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000)

# Sunucu IP ve port bilgileri
server_ip = "10.1.2.159"
server_port = 6666

# Kamerayı başlat
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Genişlik
cap.set(4, 480)  # Yükseklik

print(f"Sending video to {server_ip}:{server_port}")

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        print("Failed to capture image.")
        break

    # Görüntüyü göster
    cv2.imshow("Img Client", img)

    # Görüntüyü sıkıştır ve baytlara dönüştür
    ret, buffer = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 30])
    if not ret:
        print("Failed to encode image.")
        continue

    x_as_bytes = pickle.dumps(buffer)
    s.sendto(x_as_bytes, (server_ip, server_port))

    # Çıkış için 'Esc' tuşuna bas
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Pencereleri kapat ve kaynakları serbest bırak
cv2.destroyAllWindows()
cap.release()