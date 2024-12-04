import cv2 as cv
import numpy as np

# rgb is a colourspace, grayscale is a colourspace, BGR also, etc.

# opencv reads images in BGR
# therefore u need to convert into RGB when combining with outside imgs
# all the weird assumptions stuff, if ur doing multi libraries j remember to inv

# also greyscale to HSV is not possible, need to transitively do it thru rgb

img = cv.imread("./Resources/photos/park.jpg")
cv.imshow("vanilla", img)

# greyscale
grey = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("grey", grey)

# bgr
bgr = cv.cvtColor(img, cv.COLOR_RGB2BGR)
cv.imshow("bgr", bgr)

# hsv
hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)
cv.imshow("hsv", hsv)

# lab
lab = cv.cvtColor(img, cv.COLOR_RGB2LAB)
cv.imshow("lab", lab)

cv.waitKey(0)