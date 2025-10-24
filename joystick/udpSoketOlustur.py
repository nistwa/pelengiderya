"""import os
from socket import *

host = "10.1.2.183"  # Sunucu adresi
port = 13000         # Sunucu portu
buf = 1024           # Veri boyutu
addr = ("10.1.2.184", 12345)  # Dinlenecek adres ve port

# UDP soketi oluştur ve bağla
UPDSock = socket(AF_INET, SOCK_DGRAM)
UPDSock.bind(addr)

print("Waiting to receive messages...")
while True:
    # Gelen mesajı al
    (data, addr) = UPDSock.recvfrom(buf)
    print("Received message: " + data.decode())
    # "exit" mesajını alırsa çık
    if data.decode() == "exit":
        break

# Soketi kapat ve çık
UPDSock.close()
os.exit(0)"""

import socket

# Sunucu ayarları
host = '0.0.0.0'  # Tüm ağlardan bağlantı kabul eder
port = 5000       # Dinlemek istediğiniz port

# Soket oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)  # Maksimum 5 bağlantı kuyrukta bekleyebilir

print(f"Sunucu {host}:{port} üzerinde dinlemede...")

while True:
    conn, addr = server_socket.accept()
    print(f"Bağlantı kuruldu: {addr}")

    # Gelen veriyi al ve işlem yap
    data = conn.recv(1024).decode('utf-8')
    if data:
        print(f"Gelen veri: {data}")
        conn.send(f"Alındı: {data}".encode('utf-8'))

    conn.close()