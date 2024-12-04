# allow you to see distribution of pixel intensity
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('cats', img)

# greyscale histogram
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grey", grey)

greyHistogram = cv.calcHist([grey], [0], None, [256], [0, 256])

plt.figure()
plt.title("grey scale histogram")
plt.xlabel("bins")
plt.ylabel("no. pixels")
plt.plot(greyHistogram)
plt.xlim([0, 256])
plt.show()

# greyscale histogram
colours = ('b', 'g', 'r')
for i, col in enumerate(colours):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)