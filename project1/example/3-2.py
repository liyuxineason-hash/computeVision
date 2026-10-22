import cv2
image = cv2.imread('../photo/school.jpg')

cv2.imshow('image', image)
b,g,r = cv2.split(image)
cv2.imshow('B',b)
cv2.imshow('G',g)
cv2.imshow('R',r)
cv2.waitKey()
cv2.destroyAllWindows()