import cv2
import numpy as np


def notting(x):
    pass


capture = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
# low
cv2.createTrackbar("LowHue", "Tracking", 0, 255, notting)
cv2.createTrackbar("LowSaturation", "Tracking", 0, 255, notting)
cv2.createTrackbar("LowValue", "Tracking", 0, 255, notting)
# upper or high
cv2.createTrackbar("UpperHue", "Tracking", 255, 255, notting)
cv2.createTrackbar("UpperSaturation", "Tracking", 255, 255, notting)
cv2.createTrackbar("UpperValue", "Tracking", 255, 255, notting)


while True:
    #frame = cv2.imread("smarties.png")
    _, frame = capture.read()
    # convert to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # sent to trackbar
    l_h = cv2.getTrackbarPos("LowHue", "Tracking")
    l_s = cv2.getTrackbarPos("LowSaturation", "Tracking")
    l_v = cv2.getTrackbarPos("LowValue", "Tracking")

    u_h = cv2.getTrackbarPos("UpperHue", "Tracking")
    u_s = cv2.getTrackbarPos("UpperSaturation", "Tracking")
    u_v = cv2.getTrackbarPos("UpperValue", "Tracking")

    # low and high of color
    low_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    # detect color
    mask = cv2.inRange(hsv, low_bound, upper_bound)
    # join color
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()
