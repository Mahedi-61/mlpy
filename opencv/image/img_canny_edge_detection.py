"""
File Name: img_canny_edge_detection.py
Project Name: MLPy
Created By: Abu Noman
Created At: 12/30/2016 12:18 AM
"""

"""Canny Edge Detection is a popular edge detection algorithm. It was developed by John F. Canny in 1986. It is a
multi-stage algorithm and we will go through each stages. 1. Noise Reduction (remove noise by 5*5 gaussian filter),
2. Finding Intensity Gradient of the Image (filter with Sobel kernel in horizontal and vertical direction,
then get edge gradient & direction from these two image), 3. Non-maximum Suppression, 4. Hysteresis Thresholding
(minVal, maxVal & connection with sure-edge)"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../resources/messi5.jpg', 0)

canny = cv2.Canny(img, 100, 200)

plt.subplot(2, 1, 1), plt.imshow(img, cmap='gray')
plt.title("Original"), plt.xticks([]), plt.yticks([])

plt.subplot(2, 1, 2), plt.imshow(canny, cmap='gray')
plt.title("Canny"), plt.xticks([]), plt.yticks([])

plt.show()

