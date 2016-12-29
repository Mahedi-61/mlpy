"""
File Name: convert_color.py
Project Name: MLPy
Created By: Abu Noman
Created At: 12/24/2016 12:34 AM
"""

import numpy as np
import cv2

bgr = np.uint8([[[255, 0, 0]]])  # BGR = BLUE
test = np.uint8([[[204, 206, 206]]])  # BGR = BLUE
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)  # HSV = 120 255 255

hsv_test = cv2.cvtColor(test, cv2.COLOR_BGR2HSV)

print hsv_test

