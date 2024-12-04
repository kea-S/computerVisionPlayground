import cv2 as cv
import numpy as np

blankMatrix = np.zeros((500, 500, 3), dtype='uint8')

blankMatrix[:, 2:200] = (0, 255, 0)
cv.imshow('cat', blankMatrix)

# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('cat', img)

circle = cv.circle(blankMatrix, (250, 250), 40, (0, 0, 255), 3)
cv.imshow('circle', circle)

text = cv.putText(blankMatrix, "hello", (250, 250), cv.FONT_HERSHEY_SIMPLEX, 1.0,
                  (250, 250, 250), 4)
cv.imshow('text', text)

cv.waitKey(0)