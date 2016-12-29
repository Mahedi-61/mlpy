import numpy as np
import cv2


img = cv2.imread('../resources/bottle.jpg', cv2.IMREAD_COLOR)

# img[55, 55] = [255, 255, 255]
# px = img[55, 55]
# roi = region of interest
# roi = img[100:500, 100:500]
# img[100:700, 100:700] = [255, 255, 255]

# select part
select = img[1000:1500, 1400:1800]
cv2.imshow('selected', select)
img[0:500, 0:400] = select
cv2.imshow('edited', img)


cv2.waitKey(0)
cv2.destroyAllWindows()

