import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Gradients
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    cv2.imshow('original', frame)
    # cv2.imshow('laplacian', laplacian)
    # cv2.imshow('sobelx', sobelx)
    # cv2.imshow('sobely', sobely)

    # Edges detection
    edges = cv2.Canny(frame, 30, 80)
    cv2.imshow('edges', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

