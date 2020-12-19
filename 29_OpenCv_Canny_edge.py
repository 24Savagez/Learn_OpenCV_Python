import cv2
import numpy as np
import matplotlib.pyplot as plt


def nothing(x):
    print(x)


cv2.namedWindow('image')
cv2.createTrackbar('Threshold01', 'image', 0, 500, nothing)
cv2.createTrackbar('Threshold02', 'image', 0, 500, nothing)

while True:
    image = cv2.imread("messi5.jpg", 0)

    pos01 = cv2.getTrackbarPos('Threshold01', 'image')
    pos02 = cv2.getTrackbarPos('Threshold02', 'image')

    canny = cv2.Canny(image, pos01, pos02)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    cv2.imshow('image', canny)

cv2.destroyAllWindows()
