import cv2 as cv

img = cv.imread('F:/Codes/OpenCV/Photos/park.jpg')
cv.imshow('Park', img)

# 1. Convert to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # BGR to Gray
cv.imshow('Gray', gray)

# 2. Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT) # (7, 7) is the kernel size and cv.BORDER_DEFAULT is the border type (optional)
cv.imshow('Blur', blur)

# Edge cascade
# Edge detection is a process that identifies the boundaries of objects in images
canny = cv.Canny(blur, 125, 175) # 125 is the lower threshold and 175 is the upper threshold
cv.imshow('Canny Edgess', canny)

# Dilating the image
# A dilation is used to thicken the edges of the object in an image
# The kernel size is the size of the structuring element used to perform the dilation
dilated = cv.dilate(canny, (7, 7), iterations=3) # iterations is the number of times the dilation is applied
cv.imshow('Dilated', dilated)

# Eroding
# Erosion is the opposite of dilation; it erodes away the boundaries of the object in an image
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
# interpolation is the algorithm used to perform the resizing
# cv.INTER_AREA is used for shrinking, cv.INTER_LINEAR is used for zooming, and cv.INTER_CUBIC is used for zooming
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
# Cropping an image is the process of selecting a region of interest from the image
# The region of interest is specified by the coordinates of the top-left corner and the bottom-right corner of the cropped image
# The format of the coordinates is img[y1:y2, x1:x2]
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)