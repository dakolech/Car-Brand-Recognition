#!/usr/bin/env python

import cv2
import sys
# Get user supplied values
imagePath = sys.argv[1]
#cascPath = sys.argv[2]
cascPath="training_out/cascade.xml"
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
w=image.shape[1]

scale=1000.0/w
image=cv2.resize(image,(0,0),fx=scale,fy=scale)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect objects in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    #minSize=(20, 20),
    #maxSize=(80,80),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} objects!".format(len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Objects found", image)
cv2.waitKey(0)
