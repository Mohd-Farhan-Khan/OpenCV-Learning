# Masking is the process of selecting a region of interest in an image. It is used to hide or show certain parts of an image.
# In this snippet, we will mask an image with a weird shape.

import cv2 as cv
import numpy as np

img = cv.imread("F:/Codes/OpenCV/Photos/cats 2.jpg")
cv.imshow("Cats", img)

# Creating a blank image with the same dimensions as the original image
# Same dimensions are used to create a mask that will be used to hide certain parts of the image
# The blank image will be used to create the mask
blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank Image", blank)


circle = cv.circle(blank.copy(), (img.shape[1] // 2 + 45, img.shape[0] // 2), 100, 255, -1) 

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("Weird Shape", weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape) # first img is the source, second img is the destination, weird_shape is the mask
cv.imshow("Weird Shaped Masked Image", masked)

cv.waitKey(0)
