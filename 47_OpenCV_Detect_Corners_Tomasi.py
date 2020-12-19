import numpy as np
import cv2

image = cv2.imread("pic1.png")

cv2.imshow('image', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(image, (x, y), 3, 255, -1)

cv2.imshow('dst', image)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
