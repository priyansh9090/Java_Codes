import cv2

cv2.namedWindow("image",cv2.WINDOW_NORMAL)
img = cv2.imread('D:\\25th Anniversary Khunti\\Camera 02\\IMG_6160.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()