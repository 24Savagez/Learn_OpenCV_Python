import cv2
import numpy as np

image1 = np.zeros((250, 500, 3), np.uint8)
image1 = cv2.rectangle(image1, (200, 0), (300, 100), (255, 255, 255), -1)
#image2 = np.full((250, 500, 3), 255, np.uint8)
#image1 = cv2.rectangle(image1, (0, 0), (250, 250), (255, 255, 255), -1)
#image2 = cv2.rectangle(image2, (200, 0), (300, 100), (0, 0, 0), -1)
#image2 = np.full((250, 500, 3), 255, dtype=np.uint8)
#image2 = cv2.rectangle(image2, (0, 0), (250, 250), (0, 0, 0), -1)
image2 = cv2.imread("image_1.png")
#cv2.imwrite('image_1.png', image1)

# bitwise
#bitAnd = cv2.bitwise_and(image2, image1)
#bitOr = cv2.bitwise_or(image2, image1)
#bitXor = cv2.bitwise_xor(image2, image1)
bitNot1 = cv2.bitwise_not(image1)
bitNot2 = cv2.bitwise_not(image2)


cv2.imshow("image1", image1)
cv2.imshow("image2", image2)

#cv2.imshow("BitAnd", bitAnd)
#cv2.imshow("BitOr", bitOr)
#cv2.imshow("BitXor", bitXor)
cv2.imshow("BitNot1", bitNot1)
cv2.imshow("BitNot2", bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()
