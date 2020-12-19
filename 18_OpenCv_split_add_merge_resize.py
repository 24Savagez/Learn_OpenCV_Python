import numpy as np
import cv2

image = cv2.imread('messi5.jpg')
image2 = cv2.imread('opencv-logo.png')

print(image.shape)  # return a tuple of number of rows,columns,and channels
print(image.size)   # return total number of pixels is accessed
print(image.dtype)  # return image datatype is obtained

b, g, r = cv2.split(image)
image = cv2.merge((b, g, r))

# copy ball
ball = image[280:340, 330:390]
image[273:333, 100:160] = ball

# resize
image = cv2.resize(image, (512, 512))
image2 = cv2.resize(image2, (512, 512))

# merge
#dst = cv2.add(image, image2)
dst = cv2.addWeighted(image, 0.3, image2, 0.8, 0)

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
