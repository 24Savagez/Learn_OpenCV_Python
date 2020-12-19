import numpy as np
import cv2

capture = cv2.VideoCapture('vtest.avi')

#kernel = cv2.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))

#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
#fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=True)

while True:
    ret, frame = capture.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    #fgmask = cv2.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG MASK Frame', fgmask)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
capture.release()
cv2.destroyAllWindows()
