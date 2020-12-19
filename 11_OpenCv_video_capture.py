import cv2

# use image from webcam
capture = cv2.VideoCapture(0)

# save video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while capture.isOpened():
    # read video
    ret, frame = capture.read()

    if ret == True:
        # show number of width and height of video
        print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # save video
        out.write(frame)

        # convert video from color to grayscale
        gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # show video
        cv2.imshow('frame', gray_video)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
out.release()
cv2.destroyAllWindows()
