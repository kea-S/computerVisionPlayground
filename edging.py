import cv2 as cv
import numpy as np

img = cv.imread("./Resources/photos/cats.jpg")

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# laplace transform?
lap = cv.Laplacian(grey, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

# sobel transform?
sobelX = cv.Sobel(grey, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(grey, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobelX, sobelY)
cv.imshow('sobelX', sobelX)
cv.imshow('sobelY', sobelY)
cv.imshow('sobelComb', combined)

# canny, multi stage: uses sobel, mostly use canny, more advanced use sobel
canny = cv.Canny(grey, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)