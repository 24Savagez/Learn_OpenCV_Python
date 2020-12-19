import cv2
import numpy as np

image = cv2.imread("Irene.jpg")
# change background
#trans_mask = image[:, :, 3] == 0
#image[trans_mask] = [255, 255, 255, 255]
# convert to gray
imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of contours = ", str(len(contours)))
print(contours[0])

cv2.drawContours(image, contours, -1, (0, 255, 255), 3)

cv2.imshow('Image', image)
cv2.imshow('Image Gray', imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()

