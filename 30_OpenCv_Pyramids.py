import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Irene.jpg")
# down
lr1 = cv2.pyrDown(image)
lr2 = cv2.pyrDown(lr1)
# up
hr2 = cv2.pyrUp(lr2)
# down
cv2.imshow('original', image)
cv2.imshow('pyrDown 1', lr1)
cv2.imshow('pyrDown 2', lr2)
# up but lose resolution
cv2.imshow('pyrUp 1', hr2)

cv2.waitKey(0)
cv2.destroyAllWindows()
