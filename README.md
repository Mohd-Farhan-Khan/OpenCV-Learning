# OpenCV Learning Project

## Overview

This repository contains materials and code samples for learning and implementing computer vision applications using OpenCV. The project is structured to progress from basic concepts to advanced techniques in image processing and computer vision.

## Project Structure

- **Basic**: Introductory OpenCV operations and concepts
- **Advanced**: Advanced techniques including face detection using Haar Cascades

## Face Detection

The project includes face detection capabilities using Haar Cascade Classifiers. The `haar_face.xml` file contains a pre-trained model for frontal face detection.

### About Haar Cascade Classifiers

Haar Cascade is a machine learning-based approach where a cascade function is trained from many positive and negative images. It is then used to detect objects in other images. The algorithm was proposed by Paul Viola and Michael Jones and is particularly effective for face detection.

### Usage

To use the face detection functionality:

1. Load the cascade classifier:
```python
import cv2

# Load the face cascade
face_cascade = cv2.CascadeClassifier('Advanced/haar_face.xml')

# Read the input image
img = cv2.imread('test_image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the result
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Additional Information

- The Haar Cascade XML file used in this project is a standard file provided by OpenCV for frontal face detection.
- Face detection performance can be adjusted by modifying parameters like `scaleFactor` and `minNeighbors`.
- For more advanced face recognition tasks, consider exploring other methods like LBPH, Eigenfaces, or deep learning approaches.

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy

## License

This project includes code from the OpenCV library, which is distributed under the Apache 2.0 License.

## References

- OpenCV Documentation: https://docs.opencv.org/
- Haar Cascades Explanation: https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
