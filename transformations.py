import cv2 as cv
import numpy as np

img = cv.imread("./Resources/photos/park.jpg")

def translate(img, x, y):
    return cv.warpAffine(img, np.float32([[1, 0, x], 
                                          [0, 1, y]]),
                                          (img.shape[1], img.shape[0]))
def scale(img, s):
    return cv.warpAffine(img, np.float32([[s, 0, 1], 
                                          [0, s, 1]]),
                                          (img.shape[1], img.shape[0]))

def naiveTranspose(img):
    return cv.warpAffine(img, np.float32([[0, 1, 1], 
                                          [1, 0, 1]]),
                                          (img.shape[0], img.shape[1]))

def rotate(img, angle, centre=None):
    h, w = img.shape[0], img.shape[1]
    print(h, w)

    if centre is None:
        centre = (w//2, h//2)

    rotMat = cv.getRotationMatrix2D(centre, angle, scale=1)

    return cv.warpAffine(img, rotMat, (w, h))
    
imgTranslate = translate(img, 50, 50)
imgScale = scale(img, 2)
imgTranspose = naiveTranspose(img)
imgRotate = rotate(img, 90)
# flip vertically and horizontally
imgFlip = cv.flip(img, -1)

cv.imshow("park", img)
cv.imshow("park translate", imgTranslate)
cv.imshow("park scale", imgScale)
cv.imshow("park transpose", imgTranspose)
cv.imshow("park rotate", imgRotate)
cv.imshow("park flip", imgFlip)

cv.waitKey(0)