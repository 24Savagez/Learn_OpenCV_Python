import cv2

#read picture{0 = gray , 1 = RGB , -1 = Normal}
img = cv2.imread("Irene.jpg",0)

#define head and show picture
cv2.imshow('ImageResult',img)

#put anykey for stop
cv2.waitKey(0)
cv2.destroyAllWindows()

#save as new picture
cv2.imwrite('Result.jpg',img)


