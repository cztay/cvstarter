from __future__ import print_function  # print for 2.7 and 3.0
import argparse
import cv2

# construct the path to the image on disk
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# dimension, NumPy array#
image = cv2.imread(args["image"])
print("width:{} pixels".format(image.shape[1]))
print("height:{} pixels".format(image.shape[0]))
print("channels:{}".format(image.shape[2]))

# display the actual image#
cv2.imshow("Image", image)  # name of the window
cv2.waitKey(0)

cv2.imwrite("newimage.jpg", image)
