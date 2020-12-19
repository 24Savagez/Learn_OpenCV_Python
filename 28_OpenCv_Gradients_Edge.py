import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("sudoku.png", cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=3)
laplacian = np.uint8(np.absolute(laplacian))

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
# merge x and y together
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'laplacian', 'sobelX', 'sobelY', 'sobelCombined']
images = [image, laplacian, sobelX, sobelY, sobelCombined]
for i in range(len(titles)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
