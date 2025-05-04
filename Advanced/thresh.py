# Thresholding is the binarization of an image. In general, we seek to convert a grayscale image to a binary image, where the pixels are either 0 or 255. A simple thresholding example is when the pixel value is greater than a certain threshold, we set it to 255, otherwise 0. There are different types of thresholding, such as simple thresholding, adaptive thresholding, and Otsu's thresholding. Simple thresholding is the most basic form of thresholding, where we specify a threshold value and the pixel values are set to 0 or 255 based on the threshold value. Adaptive thresholding is a more advanced form of thresholding, where the threshold value is calculated for smaller regions of the image. Otsu's thresholding is a more advanced form of thresholding, where the threshold value is calculated based on the histogram of the image.

import cv2 as cv

img = cv.imread("F:/Codes/OpenCV/Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Simple Thresholding:

# cv.threshold(image, threshold value, max value, threshold type)
# Threshold types: cv.THRESH_BINARY, cv.THRESH_BINARY_INV, cv.THRESH_TRUNC, cv.THRESH_TOZERO, cv.THRESH_TOZERO_INV
# cv.THRESH_BINARY: If pixel value is greater than the threshold, set it to max value, otherwise 0
# cv.THRESH_BINARY_INV: If pixel value is greater than the threshold, set it to 0, otherwise max value
# cv.THRESH_TRUNC: If pixel value is greater than the threshold, set it to the threshold value, otherwise pixel value
# cv.THRESH_TOZERO: If pixel value is greater than the threshold, keep the pixel value, otherwise set it to 0
# cv.THRESH_TOZERO_INV: If pixel value is greater than the threshold, set it to 0, otherwise keep the pixel value

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
  # If pixel value is greater than 150, set it to 255, otherwise 0
cv.imshow("Simple Thresholded", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)  # If pixel value is greater than 150, set it to 0, otherwise 255
cv.imshow("Simple Thresholded Inverse", thresh_inv)


# Adaptive Thresholding:

# cv.adaptiveThreshold(image, max value, adaptive method, threshold type, block size, constant)
# Adaptive methods: cv.ADAPTIVE_THRESH_MEAN_C, cv.ADAPTIVE_THRESH_GAUSSIAN_C
# cv.ADAPTIVE_THRESH_MEAN_C: Mean of the neighborhood area
# cv.ADAPTIVE_THRESH_GAUSSIAN_C: Weighted sum of the neighborhood area
# Block size: Size of the neighborhood area
# Constant: A constant subtracted from the weighted sum of the neighborhood area

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow("Adaptive Thresholding", adaptive_thresh)

cv.waitKey(0)
