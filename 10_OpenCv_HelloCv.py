import cv2

# import image to program
image_origin = cv2.imread('lena.jpg', 0)

# show type of image
#print(image_origin)

# show image
cv2.imshow('image', image_origin)

k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    # write or copy image
    cv2.imwrite('lena_copy_01.jpg', image_origin)
    cv2.destroyAllWindows()




