import cv2
import datetime
capture = cv2.VideoCapture(0)

#capture.set(3, 640)
#capture.set(4, 480)
#print(capture.get(3), capture.get(4))

while capture.isOpened():
    ret, frame = capture.read()
    if ret == True:
        # put text or datetime on video
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+str(capture.get(3)) + 'Height: '+str(capture.get(4))

        date_time = str(datetime.datetime.now())
        frame = cv2.putText(frame, date_time, (10, 50), font, 1,
                            (0, 255, 255), 2, cv2.LINE_AA)
        
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()


