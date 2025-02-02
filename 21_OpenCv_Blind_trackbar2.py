import numpy as np
import cv2


def nothing(x):
    print(x)


# create a black image,a window
cv2.namedWindow('image')

cv2.createTrackbar('CP', 'image', 10, 400, nothing)


switch = 'color/gray'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    image = cv2.imread('lena.jpg')
    pos = cv2.getTrackbarPos('CP', 'image')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, str(pos), (50, 150), font, 6, (0, 0, 255), 10)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image = cv2.imshow('image', image)

cv2.destroyAllWindows()
