import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('park', img)

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

# bitwise and
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('and', bitwise_and)

# bitwise xor
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('xor', bitwise_xor)

# bitwise xor
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('not rectangle', bitwise_not)

cv.waitKey(0)