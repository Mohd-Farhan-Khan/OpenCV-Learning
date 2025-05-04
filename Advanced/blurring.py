import cv2 as cv

img = cv.imread("F:/Codes/OpenCV/Photos/cats.jpg")
cv.imshow("Cats", img)

# Averaging Blur (Simple Blur) -> Takes the average of all the pixels in the kernel and replaces the center pixel with the average
# The kernel size must be odd numbers (3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, ...)
# The larger the kernel size, the more the blur
average = cv.blur(img, (3, 3))
cv.imshow("Average Blur", average)


# Gaussian Blur -> Similar to the average blur but the kernel is not a box, it's a Gaussian curve (bell curve)
# The average blur is a subset of Gaussian blur (when the standard deviation is 0) -> The larger the standard deviation, the more the blur
# The average blur is faster than the Gaussian blur because the Gaussian blur has to calculate the Gaussian curve
# The Gaussian blur is more natural than the average blur
# The average in Gaussian blur is weighted (the center pixel has more weight than the other pixels)
gauss = cv.GaussianBlur(img, (3, 3), 0)  # The third parameter is the standard deviation
cv.imshow("Gaussian Blur", gauss)


# Median Blur -> Takes the median of all the pixels in the kernel and replaces the center pixel with the median
# The median blur is good for removing salt and pepper noise (black and white dots)
# The median blur is slower than the average blur and the Gaussian blur
# The median blur is good for removing noise but it's not good for blurring the image
median = cv.medianBlur(img, 3)  # Thw second parameter is the kernel size
cv.imshow("Median Blur", median)


# Bilateral Blur -> Keeps the edges sharp while blurring the rest of the image
# The bilateral blur is good for removing noise while keeping the edges sharp
# The bilateral blur is slower than the average blur, the Gaussian blur, and the median blur
# The bilateral blur has two sigma values (one for the color and one for the space)
# The color sigma is the standard deviation in the color space
# The space sigma is the standard deviation in the coordinate space
bilateral = cv.bilateralFilter(
    img, 10, 35, 25
)  # The second parameter is the diameter of the pixel neighborhood
# The third parameter is the color sigma (the larger the value, the more the blur)
# The fourth parameter is the space sigma (the larger the value, the more the blur)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
