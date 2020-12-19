import cv2

# input name's video
cap = cv2.VideoCapture("Video.mp4")
# read and recorde
while True:
    ret, frame = cap.read()
    # show normal
    #cv2.imshow('frame',frame)
    # convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # show gray
    cv2.imshow('frame', gray)

    # Stop Read
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
