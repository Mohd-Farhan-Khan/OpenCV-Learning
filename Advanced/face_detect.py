import cv2 as cv

img = cv.imread("F:/Codes/OpenCV/Photos/group 1.jpg")
cv.imshow("Group of 5 people", img)

# Face detection doesn't involve color, so we convert the image to grayscale to make it easier for the algorithm to detect faces
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray People", gray)

# Load the Haar Cascade file
# cv.CascadeClassifier("haar_face.xml") is a pre-trained model that comes with OpenCV
haar_cascade = cv.CascadeClassifier("haar_face.xml")


# scaleFactor: How much the image size is reduced at each image scale
# minNeighbors: How many neighbors each candidate rectangle should have to retain it
# minSize: Minimum possible object size. Objects smaller than this are ignored
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1) # Returns a list of rectangles where faces are detected 

print(f"Number of faces found = {len(faces_rect)}")

# Draw rectangles around the faces
for x, y, w, h in faces_rect: # x, y are the top left corner of the rectangle, w, h are the width and height of the rectangle
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("Detected Faces", img)


cv.waitKey(0)
