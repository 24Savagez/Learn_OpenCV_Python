import numpy as np
import cv2


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycolor_image = np.zeros((256, 256, 3), np.uint8)

        mycolor_image[:] = [blue, green, red]

        cv2.imshow('color', mycolor_image)


#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('messi5.jpg')
cv2.imshow('image', img)

points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
