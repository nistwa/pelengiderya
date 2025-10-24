import socket

# Sunucu için IP ve port ayarları
SERVER_IP = '192.168.1.33'
SERVER_PORT = 12345

# UDP soketi oluşturuluyor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sunucunun bağlanacağı IP ve port
server_socket.bind((SERVER_IP, SERVER_PORT))
print(f"Sunucu {SERVER_IP}:{SERVER_PORT} adresinde dinliyor...")

while True:
    # Veriyi alma
    data, addr = server_socket.recvfrom(1024)  # 1024 byte'a kadar veri alabilir
    print(f"Alınan veri: {data.decode()} from {addr}")
"""
    # Veri gönderildikten sonra cevap gönderme
    response = "Veri alındı"
    server_socket.sendto(response.encode(), addr)"""