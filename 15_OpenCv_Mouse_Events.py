import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ',' + str(y)
        cv2.putText(image, strXY, (x, y), font, 0.5, (255, 255, 0), 2)
        cv2.imshow('image', image)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = image[y, x, 0]
        green = image[y, x, 1]
        red = image[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(image, strBGR, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow('image', image)


#image = np.zeros((512, 512, 3), np.uint8)
image = cv2.imread('messi5.jpg')
cv2.imshow('image', image)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
