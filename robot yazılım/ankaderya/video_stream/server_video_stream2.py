import cv2
import socket
import struct
import pickle

def main():
    # Sunucu bilgileri
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 9999))  # Tüm ağ arayüzlerinde 9999 portunda dinle
    server_socket.listen(5)
    print("Sunucu dinliyor...")

    # Kamerayı başlat
    camera = cv2.VideoCapture(0)  # 0, varsayılan kamerayı seçer

    while True:
        conn, addr = server_socket.accept()
        print(f"Bağlantı kabul edildi: {addr}")

        try:
            while True:
                ret, frame = camera.read()
                if not ret:
                    break
                
                # Frame'i JPEG formatında sıkıştır
                ret, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
                data = pickle.dumps(buffer)
                
                # Veri uzunluğunu ve veriyi gönder
                message_size = struct.pack("Q", len(data))  # Veri uzunluğunu hesapla
                conn.sendall(message_size + data)

        except (BrokenPipeError, ConnectionResetError):
            print("Bağlantı kesildi.")
        finally:
            conn.close()

    camera.release()
    server_socket.close()

if __name__ == "__main__":
    main()
