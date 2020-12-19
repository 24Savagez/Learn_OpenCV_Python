import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("lena.jpg")
layer = image.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('upper gaussian pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow('original', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
