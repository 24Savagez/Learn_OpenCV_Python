import cv2
import numpy as np

image = cv2.imread("shapes.jpg")
imGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thrash = cv2.threshold(imGray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(image, [approx], 0, (0, 0, 0), 5)

    x = approx.ravel()[0]
    y = approx.ravel()[1] - 7

    # define name of Geometric
    if len(approx) == 3:
        cv2.putText(image, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if 0.95 <= aspectRatio <= 1.05:
            cv2.putText(image, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(image, "Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(image, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 6:
        cv2.putText(image, "Hexagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 8:
        cv2.putText(image, "Kite", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv2.putText(image, "Star", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(image, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))


cv2.imshow('shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
