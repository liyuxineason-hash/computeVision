import cv2
import numpy as np
img = cv2.imread('../photo/school.jpg')
img = cv2.resize(img, (0,0), fx=1/2, fy=1/2)
rows = len(img)
cols = len(img[0])

pl=np.float32([[0,0],[cols-1,0],[0,rows-1,cols-1]])
