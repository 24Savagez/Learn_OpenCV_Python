import cv2

# define
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
noseCascade = cv2.CascadeClassifier("Nariz.xml")
mouthCascade = cv2.CascadeClassifier("Mouth.xml")


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
        coords = [x, y, w, h]
    return img, coords


def detect(img, faceCascade, eyeCascade, noseCascade, mouthCascade):
    img, coords = draw_boundary(img, faceCascade, 1.1, 10, (0, 0, 255), "Face")
    img, coords = draw_boundary(img, eyeCascade, 1.1, 10, (255, 0, 0), "Eye")
    img, coords = draw_boundary(img, noseCascade, 1.1, 10, (0, 255, 0), "Nose")
    img, coords = draw_boundary(img, mouthCascade, 1.1, 10, (0, 255, 255), "Mouth")
    return img


# read video
cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    # call function
    frame = detect(frame, faceCascade, eyeCascade, noseCascade, mouthCascade)
    cv2.imshow('frame', frame)
    # stop detect
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
