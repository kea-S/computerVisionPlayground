# contours != edges in mathematics but can be treated as such

import cv2 as cv
import numpy as np

img = cv.imread("./Resources/photos/cats.jpg")

# has to be shape langsung
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("blank", blank)

# convert to greyscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blurred = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)

# canny-fy
canny = cv.Canny(blurred, 125, 175)
cv.imshow('Canny', canny)

# # anoter way instead of using canny is threshold
# ret, thresh = cv.threshold(grey, 125, 255, cv.THRESH_BINARY)
# cv.imshow("threshed", thresh)

# contours and hierarchies
# looks at all the edges (easier if canny and greyscale and shit)
# returns contours: py list of all coords of contours found in image
# hierarchies: hierarchy of contours, out of scope but fun to research
# cv.RETR_LIST is a mod, returns all countours, sibling sare external and tree
# contour approx method (chain...), approxes contours, none does nothing
# simple compresses all contours in a way that it makes the most sense
# e.g. if u have a line chain approx none returns all coords in that line
# while simple gets two endpoints only (since thats all u need to reconstruct)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# below is no. of contours found
print(len(contours))

cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow("contours", blank)

cv.waitKey(0)