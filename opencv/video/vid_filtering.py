""" This script is using for filtering image/videos """

import numpy as np
import cv2

# testing BGR to HSV conversion
# green = np.uint8([[[0, 255, 0]]])
# hsv = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
# print hsv


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # hue(color), saturation(distance from center), value(lightness/brightness)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # print hsv

    lower_color = np.array([50, 100, 100])
    upper_color = np.array([70, 255, 255])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("original", frame)
    # cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
