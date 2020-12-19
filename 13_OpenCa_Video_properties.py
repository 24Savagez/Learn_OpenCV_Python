import cv2

capture = cv2.VideoCapture(0)

# original set from webcam
print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# set width and height
capture.set(3, 352)
capture.set(4, 288)
# show number of WxH
print(capture.get(3))
print(capture.get(4))

while capture.isOpened():
    ret, frame = capture.read()
    if ret == True:
        gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray_video)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
