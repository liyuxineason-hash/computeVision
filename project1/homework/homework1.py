import cv2 #导入cv库
XueXiao = cv2.imread("../photo/school.jpg", 0) #灰度模式读取图像
XueXiao1 = cv2.imread("../photo/school.jpg", -1) #读取完整图像，包括alpha

XueXiao = cv2.resize(XueXiao,None,fx=2,fy=0.5) #宽放大到原来2倍，高缩小到缩小到原来1/2。
cv2.imshow("school",XueXiao) #显示XueXiao图像


