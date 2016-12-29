import numpy as np
import cv2

img = cv2.imread('../resources/threshold.jpg')
height, width, channel = img.shape

img = cv2.medianBlur(img, 5)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.resize(img, (600, 400))

ret, threshold = cv2.threshold(img, 15, 255, cv2.THRESH_BINARY)
# grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
a_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
g_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("original", cv2.resize(img, (400*(height/width), 400)))
cv2.imshow("threshold", cv2.resize(threshold, (400*(height/width), 400)))
cv2.imshow("a_threshold", cv2.resize(a_threshold, (400*(height/width), 400)))
cv2.imshow("g_threshold", cv2.resize(g_threshold, (400*(height/width), 400)))

cv2.waitKey(0)
cv2.destroyAllWindows()
