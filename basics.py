import cv2 as cv

img = cv.imread("./Resources/photos/park.jpg")

# cv.imshow('Cat', img)

# # convert to greyscale
# grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grey', grey)

# blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)

canny = cv.Canny(img, 125, 125)
cv.imshow('Canny', canny)

cannyBlur = cv.Canny(blur, 125, 125)
cv.imshow('Canny Blur', cannyBlur)

# dilating image
dilated = cv.dilate(cannyBlur, (3, 3), iterations=1)
cv.imshow('Dilated image', dilated)

# eroding image
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded image', eroded)

# cropping image
cropped = img[100:400, 200:300]
cv.imshow('cropped image', cropped)


cv.waitKey(0)