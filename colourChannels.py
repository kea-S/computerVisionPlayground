import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('park', img)

b, g, r = cv.split(img)

# colour channels gone! 3d -> 2d
new = cv.cvtColor(b, cv.COLOR_GRAY2RGB)
cv.imshow("blue", new)

merged = cv.merge([b, g, r])
cv.imshow("reconstructed", merged)

blankMatrix = np.zeros((427, 640), dtype='uint8')

# reconstructed only one colour
mergedBlue = cv.merge([b, blankMatrix, blankMatrix])
cv.imshow("reconstructed blue", mergedBlue)

cv.waitKey(0)