from __future__ import print_function
from face_library.facedetector import FaceDetector
import imutils
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="path to where the face cascade resides")
args = vars(ap.parse_args())

# construct the face detetion
fd = FaceDetector(args["face"])
camera = cv2.VideoCapture(0)

# main loop
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()
	# resize the frame and convert it to grayscale
	frame = imutils.resize(frame, width=300)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# detect eyes in the image
	faceRects = fd.detect(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))
	frameClone = frame.copy()
	# loop over the face bounding boxes and draw them	
	for (x, y, w, h) in faceRects:
		cv2.rectangle(frameClone, (x, y), (x +w, y + h), (0, 255, 0), 2)

	print("I found {} face(s)".format(len(faceRects)))

	cv2.imshow("Faces", frameClone)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

camera.release()
cv2.destroyAllWindows()
