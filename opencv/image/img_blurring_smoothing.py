"""
File Name: img_blurring_smoothing.py
Project Name: MLPy
Created By: Abu Noman
Created At: 12/24/2016 12:19 AM
"""

import cv2
import numpy as np

img = cv2.imread('../resources/bottle.jpg')
height, width, channel = img.shape
cv2.imshow('image', cv2.resize(img, (400*(height/width), 400)))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# HSV (BLUE) = 120, 255, 255
# define range of blue color in HSV
LOWER = np.array([100, 50, 50])  # H-10 for lower color
UPPER = np.array([150, 255, 255])  # H+10 for upper color

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, LOWER, UPPER)

# Bitwise-AND mask and original image
only_blues = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('only_blues', cv2.resize(only_blues, (400*(height/width), 400)))

kernel = np.ones((15, 15), np.float32)/255
smooth = cv2.filter2D(only_blues, -1, kernel)

cv2.imshow('smooth', cv2.resize(smooth, (400*(height/width), 400)))

blur = cv2.GaussianBlur(only_blues, (15, 15), 0)
cv2.imshow('Gaussian Blurring', cv2.resize(blur, (400*(height/width), 400)))

median = cv2.medianBlur(only_blues, 15)
cv2.imshow('Median Blur', cv2.resize(median, (400*(height/width), 400)))

k = cv2.waitKey(0) & 0xFF
if k == 27:  # ESC key
    cv2.destroyAllWindows()



