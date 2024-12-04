import cv2 as cv

# img = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow('cat', img)

def rescaleFrame(frame, scale=0.75):
    h = int(frame.shape[0] * scale)
    w = int(frame.shape[1] * scale)

    dims = (w, h)

    # INTER AREA good for shrinking images, but if u want to expand
    # use INTER_LINEAR or INTER_CUBIC (cubic better quality but more expensive)
    return cv.resize(frame, dims, interpolation=cv.INTER_AREA)

def changeRes(w, h):
    capture.set(3, w)
    capture.set(4, h)

capture = cv.VideoCapture(0)

changeRes(512, 512)

while True:
    isTrue, frame = capture.read()

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()