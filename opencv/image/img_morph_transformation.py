# coding=utf-8
"""
File Name: img_morph_transformation.py
Project Name: MLPy
Created By: Abu Noman
Created At: 12/28/2016 12:55 AM
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

"""Morphological transformations are some simple operations based on the image shape. It is normally performed on
binary images. It needs two inputs, one is our original image, second one is called structuring element or kernel
which decides the nature of operation. Two basic morphological operators are Erosion and Dilation. Then its variant
forms like Opening, Closing, Gradient etc also comes into play. """

img = cv2.imread('../resources/binary_j.png')

plt.subplot(321), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

# Erosion
"""A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1,
otherwise it is eroded (made to zero). So what happens is that, all the pixels near boundary will be discarded depending
upon the size of kernel. So the thickness or size of the foreground object decreases or simply white region decreases in
the image. It is useful for removing small white noises, detach two connected objects etc."""
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

plt.subplot(322), plt.imshow(erosion), plt.title('Erosion')
plt.xticks([]), plt.yticks([])

# Dilation
"""It is just opposite of erosion. Here, a pixel element is ‘1’ if at least one pixel under the kernel is ‘1’. So it
increases the white region in the image or size of foreground object increases. Normally, in cases like noise
removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So
we dilate it. Since noise is gone, they won’t come back, but our object area increases. It is also useful in joining
broken parts of an object. """

dilation = cv2.dilate(erosion, kernel, iterations=1)
plt.subplot(323), plt.imshow(dilation), plt.title('Dilation')
plt.xticks([]), plt.yticks([])

# Opening
"""Opening is just another name of erosion followed by dilation. It is useful in removing noise"""
img_opening = cv2.imread('../resources/binary_j_opening.png')
opening = cv2.morphologyEx(img_opening, cv2.MORPH_OPEN, kernel)
plt.subplot(324), plt.imshow(img_opening), plt.title('Opening_Original')
plt.xticks([]), plt.yticks([])
plt.subplot(325), plt.imshow(opening), plt.title('Opening')
plt.xticks([]), plt.yticks([])

# Closing
"""Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the
foreground objects, or small black points on the object. """
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
plt.subplot(326), plt.imshow(closing), plt.title('Closing')
plt.xticks([]), plt.yticks([])

plt.show()

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
