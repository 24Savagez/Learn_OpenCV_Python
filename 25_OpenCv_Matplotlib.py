from matplotlib import pyplot as plt
import cv2

image = cv2.imread('lena.jpg', -1)
cv2.imshow("Image", image)

# matplotlib read image from RGB / CV2 read image for BGR
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.xticks([]), plt.yticks([])


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
