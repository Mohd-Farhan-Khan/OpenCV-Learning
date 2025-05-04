# Contours are the boundaries of the object in an image. They are useful in shape analysis and object detection and recognition.
# From mathematical perspective, contours are the curve joining all the continuous points along the boundary of an object.

import cv2 as cv
import numpy as np

img = cv.imread("F:/Codes/OpenCV/Photos/park.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape, dtype="uint8") #  shape
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blurring the image to reduce noise so that the contours can be detected more accurately
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

# Thresholding is used to convert an image to a binary image
# In thresholding, the pixels of an image are converted to either black or white based on a threshold value
# If value is less than 125 (threshold value), it is set to 0 (black) and if it is greater than 125, it is set to 255 (white)
# The function takes in the image, the threshold value, the maximum value, and the thresholding type as arguments
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)


# findContours function is used to find the contours in an image
# The function takes in the image, the retrieval mode, and the approximation method as arguments
# The function return a tuple of contours and heirarchies
# cv.RETR_LIST retrieves all the contours
# cv.CHAIN_APPROX_SIMPLE compresses the contours by removing redundant points and only storing the end points and return only those contours that make sense
# cv.RETR_EXTERNAL retrieves only the external contours
# cv.CHAIN_APPROX_NONE retrieves all the contours without compressing them
# cv.RETR_TREE retrieves all the contours and creates a full hierarchy of nested contours
# cv.RETR_CCOMP retrieves all the contours and organizes them into two-level hierarchy
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contour(s) found!")


# Draw the contours on the blank image
# Arguments: image, contours, index of the contour to draw (-1 to draw all contours), color, thickness
# The thickness of -1 will fill the contour
# the index of the contour to draw can be changed to draw a specific contour
# index = 0 will draw the first contour in the list, -1 will draw all the contours and similarly, any other index will draw that specific contour
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)
