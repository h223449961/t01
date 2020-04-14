import cv2
OringinalImage = cv2.imread('i.jpg')
GrayImage = cv2.imread('i.jpg',0)
cv2.imshow('01', OringinalImage)
cv2.imshow('02', GrayImage)
cv2.waitKey(0)
cv2.destroyAllWindows