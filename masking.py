import cv2 as cv
import numpy as np

# img = cv.imread('Resources/Photos/cats.jpg')
# cv.imshow('cats', img)

# # just play around with copying over the entirety of the shape r only up to colours
# blank = np.zeros(img.shape[:2], dtype='uint8')

# circleMask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

# crosshair = cv.bitwise_and(img, img, mask=circleMask)
# cv.imshow('crosshair', crosshair)

# cv.waitKey(0)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    blank = np.zeros(frame.shape[:2], dtype= np.uint8)
    circleMask = cv.circle(blank, (frame.shape[1] // 2, frame.shape[0] // 2), 150, 255, -1)
    cv.imshow('mask', circleMask)

    video_and = cv.bitwise_and(frame, frame , mask=circleMask)

    cv.imshow('video', video_and)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()