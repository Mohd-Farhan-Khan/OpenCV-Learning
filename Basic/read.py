import cv2 as cv

# Reading Images
img = cv.imread("F:/Codes/OpenCV/Photos/cat.jpg") # This will read the image
cv.imshow("Cat", img) 

cv.waitKey(0)  # 0 means that the window will be open until any key is pressed

# Reading Videos
capture = cv.VideoCapture("Videos/dog.mp4")

while True:
    isTrue, frame = (capture.read())  # isTrue is a boolean value that tells us if the frame was read correctly
    cv.imshow("Video", frame) 

    if cv.waitKey(20) & 0xFF == ord("d"):  # If the letter d is pressed, the video will stop
        break

capture.release() # This will release the video
cv.destroyAllWindows() # This will close all the windows
