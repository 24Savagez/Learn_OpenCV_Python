import numpy as np
import cv2

image = cv2.imread("pic1.png")

cv2.imshow('image', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

det = cv2.dilate(dst, None)

image[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', image)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
