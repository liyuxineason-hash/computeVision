import cv2
# image = cv2.imread("photo/school.jpg",-1)
XueXiao = cv2.imread("../photo/school.jpg", 0)
# image = cv2.imread("photo/school.jpg",1)

cv2.imshow("school",XueXiao)
k = cv2.waitKey()
if k== ord('s'):
   cv2.imwrite("D:/computeVision/picture/Xuexiao.png",XueXiao)
cv2.destroyAllWindows()