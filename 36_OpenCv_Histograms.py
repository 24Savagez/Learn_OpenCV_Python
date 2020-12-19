import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('lena.jpg', 0)
#image = np.zeros((200, 200), np.uint8)
#cv2.rectangle(image, (0, 100), (200, 200), 255, -1)
#cv2.rectangle(image, (0, 50), (100, 100), 127, -1)

hist = cv2.calcHist([image], [0], None, [256], [0, 256],)
plt.plot(hist)

#b, g, r = cv2.split(image)
#cv2.imshow('image', image)
#cv2.imshow("b", b)
#cv2.imshow("g", g)
#cv2.imshow("r", r)

#plt.hist(image.ravel(), 256, [0, 256])
#plt.hist(b.ravel(), 256, [0, 256])
#plt.hist(g.ravel(), 256, [0, 256])
#plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
