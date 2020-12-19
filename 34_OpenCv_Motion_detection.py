import cv2
import numpy as np

capture = cv2.VideoCapture("vtest.avi")

ret, frame1 = capture.read()
ret, frame2 = capture.read()

while capture.isOpened():
    # find different from 1 and 2
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        # get x y w h from contour
        (x, y, w, h) = cv2.boundingRect(contour)

        # define area for draw if less than 700 don't draw
        if cv2.contourArea(contour) < 900:
            continue
        # draw rectangle on object
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # put text on video
        cv2.putText(frame1, "Status:{}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # draw around object
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = capture.read()

    if cv2.waitKey(40) == 27:
        break

capture.release()
cv2.destroyAllWindows()
