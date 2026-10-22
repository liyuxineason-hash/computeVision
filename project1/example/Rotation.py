import cv2
import numpy as np
img = cv2.imread('../photo/school.jpg')
rows = len(img)
cols = len(img[0])
cent=(rows/2,cols/2)
M = cv2.getRotationMatrix2D(cent,-30,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('dst',dst)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()