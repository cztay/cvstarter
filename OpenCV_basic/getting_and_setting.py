from __future__ import print_function  # print for 2.7 and 3.0
import argparse
import cv2

# construct the path to the image on disk
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the actual image off from disk and display 
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

print("width:{} pixels".format(image.shape[1]))
print("height:{} pixels".format(image.shape[0]))
print("channels:{}".format(image.shape[2]))

# BRG at (x,y)=(50,50)
(b, g, r) = image[50, 50]
print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image[0:30, 0:30] = (0, 0, 255) # that 30X30 area become red colour
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0) # green color

# display the actual image
cv2.imshow("New_image", image)  # name of the window
cv2.waitKey(0)

cv2.imwrite("newimage.jpg", image)
