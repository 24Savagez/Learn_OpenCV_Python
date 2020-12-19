import cv2

# define
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# function
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    # covert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
    coords = []
    # create rectangle
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    return img


def detect(img, faceCascade):
    img = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "First")
    return img


# read video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # call function
    frame = detect(frame, faceCascade)
    cv2.imshow('frame', frame)
    # stop detect
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

