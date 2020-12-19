import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread("lena.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 3)

cv2.imshow('image', image)
cv2.waitKey(0)
