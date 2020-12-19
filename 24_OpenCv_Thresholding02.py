import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('sudoku.png', 0)
_, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
th1 = cv2.cvtColor(th1, cv2.COLOR_BGR2RGB)
th2 = cv2.cvtColor(th2, cv2.COLOR_BGR2RGB)
th3 = cv2.cvtColor(th3, cv2.COLOR_BGR2RGB)

plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title("Original")

plt.subplot(2, 2, 2)
plt.imshow(th1)
plt.title("Binary")

plt.subplot(2, 2, 3)
plt.imshow(th2)
plt.title("Mean_C")

plt.subplot(2, 2, 4)
plt.imshow(th3)
plt.title("Gaussian_C")

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
