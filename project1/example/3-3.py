import cv2                                          #导入OpenCV库
import numpy as np                                  #导入numpy库
image=cv2.imread("../photo/school.jpg")                      #读取图像
cv2.imshow("BGR",image)                             #显示BGR图像
b,g,r=cv2.split(image)                              #拆分BGR图像中的通道
# cv2.imshow("B",b)                                   #显示B通道的灰度图
imgZeros=np.zeros_like(image)                       #创建与image相同形状的黑色图像
imgZeros[:,:,1]=b                                   #在黑色图像模板添加蓝色分量b
cv2.imshow("channel B",imgZeros)	#显示扩展后的图像
cv2.waitKey()
cv2.destroyAllWindows()

