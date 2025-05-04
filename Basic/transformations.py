import cv2 as cv
import numpy as np

img = cv.imread("F:/Codes/OpenCV/Photos/park.jpg")
cv.imshow("Park", img)


# Translation (Shifting an image along the x and y axis)
def translate(img, x, y):
    # translation matrix
    # The matrix is a 2x3 matrix that defines how much the image should be shifted along the x and y axes
    # The matrix is defined as follows:
    # | 1 0 x |
    # | 0 1 y |
    # where # x is the number of pixels to shift along the x-axis and y is the number of pixels to shift along the y-axis
    # and 1 and 0 are scaling factors that are used to scale the image
    # np.float32 is used to convert the matrix to a floating-point number (32-bit) so that it can be used in the warpAffine function
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    # The warAffine function is used to apply the translation matrix to the image
    return cv.warpAffine(img, transMat, dimensions)


# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow("Translated", translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]  # Get the height and width of the image

    # None -> centre of the image
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    # The rotation matrix is a 2x3 matrix that defines how much the image should be rotated
    # 1.0 is the scaling factor
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)
cv.imshow("Rotated", rotated)

rotated_rotated = rotate(img, -90)
cv.imshow("Rotated Rotated", rotated_rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# Flipping
# 0 -> fliiping vertically
# 1 -> flipping horizontally
# -1 -> flipping both horizontally and vertically
flip = cv.flip(img, -1)
cv.imshow("Flip", flip)

# Cropping
# y1:y2, x1:x2 (top-left corner, bottom-right corner)
cropped = img[200:400, 300:400]  # 200:400 is the y-axis and 300:400 is the x-axis
cv.imshow("Cropped", cropped)


cv.waitKey(0)
