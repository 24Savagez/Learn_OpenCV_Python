import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Noise_salt_and_pepper.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

kernal = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(image, -1, kernal)
blur = cv2.blur(image, (5, 5))
gblur = cv2.GaussianBlur(image, (5, 5), 0)
median = cv2.medianBlur(image, 5)
bilateralFilter = cv2.bilateralFilter(image, 9, 75, 75)


titles = ['image', '2D_Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [image, dst, blur, gblur, median, bilateralFilter]
for i in range(len(titles)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
