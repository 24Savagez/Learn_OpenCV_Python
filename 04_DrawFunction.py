import cv2

img = cv2.imread('Irene.jpg')
#line
#img = cv2.line(img,(0,0),(255,255),(0,0,255),5)
#arrow
#img = cv2.arrowedLine(img,(0,0),(400,400),(255,0,0),5)
#rectangle
#img = cv2.rectangle(img,(394,0),(510,128),(0,0,255),5)
#circle
#img = cv2.circle(img,(447,63),(63),(0,255,0),2)
#text
img = cv2.putText(img,"FirstOnez",(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)


cv2.imshow("Result2",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
