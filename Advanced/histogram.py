# Histograms are a great way to visualize the distribution of pixel intensities in an image. They can be used to analyze the contrast, brightness, and intensity distribution of an image. Histograms are also useful for thresholding an image, which can be used to separate objects from the background.

# Histograms can be created for both grayscale and color images. For grayscale images, the histogram will show the distribution of pixel intensities. For color images, the histogram will show the distribution of pixel intensities for each color channel (red, green, and blue).


import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("F:/Codes/OpenCV/Photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask) # first img is the source, second img is the destination, mask is the mask
cv.imshow("Mask", masked)

# Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )
# [0] is the channel, mask is the mask, [256] is the number of bins, [0,256] is the range of the bins (0-256)

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Colour Histogram

plt.figure()
plt.title("Colour Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ("b", "g", "r") # vlue, green, red
for i, col in enumerate(colors): # enumerate gives the index of any colour in the tuple (i is the index, col is the colour)
    hist = cv.calcHist([img], [i], mask, [256], [0, 256]) # [i] is the channel, mask is the mask, [256] is the number of bins, [0,256] is the range of the bins (0-256)
    plt.plot(hist, color=col) 
    plt.xlim([0, 256]) # range of the bins

plt.show()

cv.waitKey(0)
