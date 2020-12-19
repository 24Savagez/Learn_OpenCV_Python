import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('j.png', cv2.IMREAD_GRAYSCALE)
#_, mask = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(image, kernal, iterations=2)
erosion = cv2.erode(image, kernal, iterations=1)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernal)
mg = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [image, image, dilation, erosion, opening, closing, mg, th]

for i in range(len(titles)):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
