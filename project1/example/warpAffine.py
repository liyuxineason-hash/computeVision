import cv2
import numpy as np
img = cv2.imread('../photo/school.jpg')
img = cv2.resize(img, (0,0), fx=1/2, fy=1/2)
rows = len(img)
cols = len(img[0])
M = np.float32([[1,0,100],
                [0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('Input',img)
cv2.imshow('Trans',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()