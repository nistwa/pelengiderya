import sys
import cv2
import pygame
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication


# Fake ServoKit Sınıfı
class FakeServoKit:
    def __init__(self, channels):
        print(f"FakeServoKit initialized with {channels} channels")

    def set_servo_angle(self, channel, angle):
        print(f"Channel {channel} angle set to {angle}")

    # Servo özellikleri için basit bir setter
    class Servo:
        def __init__(self):
            self.angle = 90

        def set_angle(self, angle):
            print(f"Setting angle to {angle}")
            self.angle = angle

    def __getattr__(self, name):
        if name == "servo":
            return [self.Servo() for _ in range(16)]


# ServoKit ayarları
kit = FakeServoKit(channels=16)

# Joystick ayarları
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Joystick bulundu: {joystick.get_name()}")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 853)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Servo açıları için QLabel
        self.angle_label = QtWidgets.QLabel(self.centralwidget)
        self.angle_label.setGeometry(QtCore.QRect(740, 190, 241, 81))
        self.angle_label.setObjectName("angle_label")
        self.angle_label.setText("Servo Açıları: CW: 0, CCW: 0")

        # Kamera görüntüsü için QLabel
        self.camera_label = QtWidgets.QLabel(self.centralwidget)
        self.camera_label.setGeometry(QtCore.QRect(90, 110, 600, 400))
        self.camera_label.setObjectName("camera_label")
        self.camera_label.setText("Kamera Görüntüsü")
        self.camera_label.setAlignment(QtCore.Qt.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


class ServoMonitorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Timer'lar
        self.angle_timer = QTimer()
        self.angle_timer.timeout.connect(self.update_angles)
        self.angle_timer.start(100)  # 100 ms'de bir güncelleme

        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self.update_camera)
        self.camera_timer.start(30)  # ~33 FPS için

        # OpenCV ile kamera başlat
        self.cap = cv2.VideoCapture(0)

    def update_angles(self):
        pygame.event.pump()

        # Joystick'ten açı hesaplama
        cw = int(90 - (joystick.get_axis(0) * 90))
        ccw = int(90 + (joystick.get_axis(0) * 90))

        # Açılara sınır koy
        cw = max(15, min(165, cw))
        ccw = max(15, min(165, ccw))

        # Servo açılarını güncelle (FakeServoKit ile)
        kit.servo[0].set_angle(cw)
        kit.servo[1].set_angle(cw)
        kit.servo[2].set_angle(ccw)
        kit.servo[3].set_angle(ccw)

        # Label'ı güncelle
        self.ui.angle_label.setText(f"Servo Açıları: CW: {cw}, CCW: {ccw}")

    def update_camera(self):
        ret, frame = self.cap.read()
        if ret:
            # OpenCV görüntüsünü PyQt için dönüştür
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            step = channel * width
            q_img = QImage(frame.data, width, height, step, QImage.Format_RGB888)

            # QLabel'e görüntüyü göster
            self.ui.camera_label.setPixmap(QPixmap.fromImage(q_img))

    def closeEvent(self, event):
        # Kamera serbest bırakılır
        self.cap.release()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServoMonitorApp()
    window.show()
    sys.exit(app.exec_())
