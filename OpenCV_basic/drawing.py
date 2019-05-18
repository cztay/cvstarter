import numpy as np
import cv2


# np.zeros method with 300x300 with 3 channels, 
# the "zeros" method fills every element in array with an initial value of zero
# we are representing our image as an RGB image with pixels in range [0,255], so we need to use an 8-bit unsigned integer. 

canvas = np.zeros((300, 300, 3), dtype="uint8")  # data type is 8-bit unisigned integer


green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)  # (picture, starting, end, colour, thickness)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# rectangle
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.rectangle(canvas, (100, 256), (225, 200), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
blue = (100, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)  # shape[0] is height, [1] is width

white = (255, 255, 255)
# 0 to 150, 25 is increment
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# beauty circle
# Draw 25 random circles by using NumPy's random number capabilities through np.random.randint function. 
for i in range(0, 25):
    radius = np.random.randint(5, high=200) # radius value in the range[5,200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()  # return a list of three numbers, size(3,) is 3 column and no limit for row. 
    pt = np.random.randint(0, high=300, size=(2,)) # random point 
    #cv2.circle(img, center, radius, color, thickness)
    cv2.circle(canvas, tuple(pt), radius, color,-1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
