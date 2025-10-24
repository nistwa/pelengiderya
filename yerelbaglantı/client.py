import socket

# Sunucunun IP ve port ayarları
SERVER_IP = '192.168.1.33'  # localhost
SERVER_PORT = 12345

# UDP soketi oluşturuluyor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Gönderilecek veri
message = "Merhaba Sunucu!"

# Veriyi sunucuya gönderme
client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
print(f"Veri gönderildi: {message}")

# Sunucudan gelen cevabı alma
response, server_addr = client_socket.recvfrom(1024)
print(f"Sunucudan gelen cevap: {response.decode()}")

# Soketi kapatma
client_socket.close()