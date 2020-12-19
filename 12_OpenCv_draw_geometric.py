import cv2
import numpy as np

# import image
#image = cv2.imread('lena.jpg', 1)

# use image from numpy
image = np.zeros([512, 512, 3], np.uint8)

# draw geometric
image = cv2.line(image, (0, 0), (255, 255), (66, 245, 149), 10)

image = cv2.arrowedLine(image, (0, 255), (255, 255), (0, 0, 255), 10)

# rectangle
'''
x1,y1-------
|           |
|           |
|           |
---------x2,y2
'''
image = cv2.rectangle(image, (384, 0), (510, 128), (255, 0, 0), 10)

image = cv2.circle(image, (447, 63), 63, (255, 255, 0), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image, 'OpenCv', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

# show image
cv2.imshow('grayscale', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
