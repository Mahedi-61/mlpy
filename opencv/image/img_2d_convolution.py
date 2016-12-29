"""
File Name: img_2d_convolution.py
Project Name: MLPy
Created By: Abu Noman
Created At: 12/28/2016 12:21 AM
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../resources/cars_road.jpg')

# cv2.imshow("original", img)

"""Filtering with the above kernel results in the following being performed: for each pixel, a 5x5 window is centered
on this pixel, all pixels falling within this window are summed up, and the result is then divided by 25. This
equates to computing the average of the pixel values inside that window """
kernel = np.ones((3, 3), np.float32)/9
dst = cv2.filter2D(img, -1, kernel)
plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
# plt.show()

# Image Blurring (Image Smoothing) - used for removing noise
blur = cv2.blur(img, (3, 3))
# plt.subplot(121), plt.imshow(img), plt.title('Original2')
# plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(blur), plt.title('Blurring')
plt.xticks([]), plt.yticks([])
plt.show()

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()

