import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('gradient.png')
# threshold
_, th1 = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)

# show image
titles = ['Original', 'Binary', 'Bi_inverse', 'Trunc', 'To_zero', 'To_zero_inv']
images = [image, th1, th2, th3, th4, th5]
for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    # delete x and y bar
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
