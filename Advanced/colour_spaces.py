# Colour spaces are different ways of representing colour in an image. The most common colour space is BGR (Blue, Green, Red) which is the default colour space in OpenCV. Other colour spaces include Grayscale, HSV (Hue, Saturation, Value), L*a*b (Lightness, a, b) and RGB (Red, Green, Blue).

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("F:/Codes/OpenCV/Photos/park.jpg")
cv.imshow("Park", img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB --> BGR", lab_bgr)

cv.waitKey(0)
