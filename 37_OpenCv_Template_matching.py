import cv2
import numpy as np

image = cv2.imread("messi5.jpg")
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template = cv2.imread("messi_face.jpg", 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(gray_img, template, cv2.TM_CCORR_NORMED)
print(res)
threshold = 0.99
loc = np.where(res >= threshold)

print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
