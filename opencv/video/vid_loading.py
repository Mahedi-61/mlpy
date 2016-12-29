import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print "cap is not opened"
    cap.open()
else:
    print "cap is already opened"

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # fgmask = fgbg.apply(frame)
    # cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
