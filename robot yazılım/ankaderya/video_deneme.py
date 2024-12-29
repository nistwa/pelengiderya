#!/usr/bin/env python3
import cv2
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
ret,img=cap.read()
cv2.imshow('img',img)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()