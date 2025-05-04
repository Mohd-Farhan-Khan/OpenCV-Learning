import cv2 as cv
import numpy as np

img = cv.imread("F:/Codes/OpenCV/Photos/park.jpg")
cv.imshow("Park", img)

blank = np.zeros(img.shape[:2], dtype="uint8") # Creating a blank image with the same dimensions as the original image (img)
# dtype="uint8" -> Unsigned integer (0 to 255) and uint8 is for 8-bit images
# img.shape[:2] -> (427, 640) -> Rows and columns of the image (excluding the channels) and since the blank image is grayscale, we don't need the channels
 
b, g, r = cv.split(img) # Splitting the image into its BGR channels 

cv.imshow("Blue_GrayScaled", b) # Displaying the Blue channel in grayscale (since it's a single channel)
cv.imshow("Green_GrayScaled", g) # Displaying the Green channel in grayscale (since it's a single channel)
cv.imshow("Red_GrayScaled", r) # Displaying the Red channel in grayscale (since it's a single channel)

blue = cv.merge([b, blank, blank]) # Merging the Blue channel with blank channels for Green and Red (to display only the Blue channel)
green = cv.merge([blank, g, blank]) # Merging the Green channel with blank channels for Blue and Red (to display only the Green channel)
red = cv.merge([blank, blank, r]) # Merging the Red channel with blank channels for Blue and Green (to display only the Red channel)


cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

print(img.shape) # (427, 640, 3) -> 427 rows, 640 columns, 3 channels (BGR) 
print(b.shape) # (427, 640) -> 427 rows, 640 columns (same as img.shape[:2]) 
print(g.shape) # (427, 640) 
print(r.shape) # (427, 640)


merged = cv.merge([b, g, r]) # Merging the split channels back together
cv.imshow("Merged Image", merged)

cv.waitKey(0)
