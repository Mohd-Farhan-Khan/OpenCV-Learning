# Gradient: Change in brightness over a pixel
# Gradients are useful for edge detection
# Laplacian: Computes the Laplacian of the image by convolving the image with the Laplacian kernel
# Sobel: Computes the gradient of the image by convolving the image with the Sobel kernel in the x and y directions
# Canny: Computes the gradient of the image and applies non-maximum suppression to thin the edges, and hysteresis thresholding to detect strong, weak, and non-relevant edges

# Which is the best edge detection algorithm?
# It depends on the application. Canny edge detection is the most commonly used edge detection algorithm, as it is more accurate and less sensitive to noise compared to other edge detection algorithms. However, the best edge detection algorithm depends on the specific requirements of the application. For example, if the application requires real-time edge detection, the Sobel operator may be more suitable due to its simplicity and efficiency. On the other hand, if the application requires high accuracy, the Laplacian operator may be more suitable due to its ability to detect fine details in the image.

import cv2 as cv
import numpy as np

img = cv.imread("F:/Codes/OpenCV/Photos/park.jpg")
cv.imshow("Park", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian:
# cv.Laplacian(image, data type)
# Laplacian is the second derivative of the image, which measures the rate of change of the gradient of the image
# The Laplacian operator is used for edge detection, as it highlights regions of rapid intensity change in the image
lap = cv.Laplacian(gray, cv.CV_64F)  # cv.CV_64F is the data type of the output image (64-bit float)
lap = np.uint8(np.absolute(lap))  # Convert the output image to 8-bit unsigned integer format
cv.imshow("Laplacian", lap)


# Sobel:
# cv.Sobel(image, data type, x order, y order)
# Sobel is used for edge detection, as it computes the gradient of the image in the x and y directions
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)  # Gradient in the x direction (horizontal)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)  # Gradient in the y direction (vertical)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Combined Sobel", combined_sobel)


# Canny
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)
cv.waitKey(0)
