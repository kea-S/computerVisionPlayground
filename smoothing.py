import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('park', img)

# gaussian blur (same like averaging, but give surrounding pixels weights)
# less blur than averaging (but more "natural"... i have no idea)
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('gausspool', gauss)

# averaging (sort of like meanpool?)
avg = cv.blur(img, (3, 3))
cv.imshow('meanpool', avg)

# median (sort of like meanpool?)
# reduces noise better
median = cv.medianBlur(img, 3)
cv.imshow('medianpool', median)

# bilateral (takes account of edges)
# so it like takes account of edges more
# larger sigmaColour, more colours thatll be considered by the blur. ???
# sigmaSpace, larger means takes account more surrounding pixels. So more blur?
# sigma space is OUTSIDE of the kernel vision
# higher params for all makes it look like median blur more
bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow('bilateralpool', bilateral)

cv.waitKey(0)