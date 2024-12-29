#!/usr/bin/env python3
from adafruit_servokit import ServoKit
import time
import board
import busio
i2c_bus1=(busio.I2C(board.SCL, board.SDA))
kit = ServoKit(channels=16,i2c=i2c_bus1)
kit.servo[0].angle=89
time.sleep(1)
kit.servo[0].angle=150
time.sleep(3)
kit.servo[0].angle=60
time.sleep(3)
kit.servo[0].angle=89
