"""
File Name: vid_blurring_smoothing.py
Project Name: MLPy
Created By: Abu Noman
Created At: 12 / 23 / 2016
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _ret, frame = cap.read()
    if not _ret:
        continue

    cv2.imshow('original', frame)
    # converting BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    print hsv

    LOWER_COLOR = np.array([240, 100, 40])  # HSV color of BGR(100, 0, 0)
    UPPER_COLOR = np.array([240, 100, 100])  # HSV color of BGR(255, 0, 0)
    # Masking [filter range of color]
    mask = cv2.inRange(hsv, LOWER_COLOR, UPPER_COLOR)
    cv2.imshow('mask', mask)

    kernel = np.ones((15, 15), np.float32)/225

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

