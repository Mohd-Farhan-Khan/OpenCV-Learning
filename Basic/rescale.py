import cv2 as cv

img = cv.imread("F:/Codes/OpenCV/Photos/cat_large.jpg")
cv.imshow("Cat", img)


def rescaleFrame(frame, scale=0.75):
    # This function will work for Images, Videos and Live Videos
    width = int(frame.shape[1] * scale) # frame.shape[1] is the width of the frame
    height = int(frame.shape[0] * scale) # frame.shape[0] is the height of the frame
    dimensions = (width, height) # dimensions is a tuple that contains the width and height

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # INTER_AREA is the interpolation method that we are using


img_resized = rescaleFrame(img) 
cv.imshow("Resized Image", img_resized) 

def changeRes(width, height): 
    # This function will work for Live Videos
    capture.set(3, width) # 3 is the width of the frame
    capture.set(4, height) # 4 is the height of the frame


capture = cv.VideoCapture("F:/Codes/OpenCV/Videos/dog.mp4")

while True:
    isTrue, frame = (capture.read())  # isTrue is a boolean value that tells us if the frame was read correctly
    cv.imshow("Video", frame)

    frame_resized = rescaleFrame(frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord("d"):  # If the letter d is pressed, the video will stop
        break

capture.release()
cv.destroyAllWindows()
