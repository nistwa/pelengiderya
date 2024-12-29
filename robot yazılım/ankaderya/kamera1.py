#!/usr/bin/env python3
import cv2

#img=cv2.imread("asfa.png")
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
ret, frame = cap.read()
#print(frame)
cv2.imshow("pencere",frame)
cv2.waitKey(0)
"""

cv2.imwrite("frame.jpg",frame)
img=cv2.imread("frame.jpg")

cv2.imshow('pencere', img)

#cv2.imshow("pencere",img)

#
if not cap.isOpened():
    print("Camera not opened")
else:
    while True:
        ret, frame = cap.read()
        if ret:
            # Process the frame using OpenCV operations
            cv2.imshow('Frame', frame)

        # Exit the loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    #cap.release()


cv2.waitKey(0)
cv2.destroyAllWindows()"""