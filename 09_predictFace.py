import cv2

# Global variable
img_id = 0
idnumber = 1

# define something
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# create name
def create_dataset(img, id, img_id):
    cv2.imwrite("Picture/001/pic." + str(id) + "." + "(" + str(img_id) + ")" + ".jpg", img)


# function
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
    # covert to gray for detect
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
    coords = []
    # create rectangle
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        id, con = clf.predict(gray[y:y + h, x:x + w])

        # check confident and defined
        if id == 1:
            if con <= 35:
                cv2.putText(img, "Cherprnag", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            else:
                cv2.putText(img, "Unknow", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        #if id == 2:
            #if con <= 35:
                #cv2.putText(img, "Bill Gates", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            #else:
                #cv2.putText(img, "Unknow", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # show percent
        if (con < 100):
            con = "   {0}%".format(round(100 - con))
        else:
            con = "   {0}%".format(round(100 - con))
        print(str(con))

        coords = [x, y, w, h]
    return img, coords


# function cut only face
def detect(img, faceCascade, img_id, clf):
    img, coords = draw_boundary(img, faceCascade, 1.1, 10, (0, 0, 255), clf)
    # define face
    if len(coords) == 4:
        id = idnumber
        # y+h x+w
        result = img[coords[1]:coords[1] + coords[3], coords[0]:coords[0] + coords[2]]
        # call fucntion name
        # create_dataset(result,id,img_id)
    return img


# read video put = name's video and 0 for webcame
cap = cv2.VideoCapture("BNK.mp4")

# file trained
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("PersonClassifierCherprang.xml")

while (True):
    ret, frame = cap.read()
    # call function
    frame = detect(frame, faceCascade, img_id, clf)
    cv2.imshow('frame', frame)
    img_id += 1
    # stop detect
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
