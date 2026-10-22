import cv2
import numpy as np
img=cv2.imread("../material/Train/photo.png")
cv2.imshow("Input",img)
#将图像的色彩空间从BGR转换为HSV
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#定义蓝色的下界数组和上界数组
lower=np.array([[100],[43],[46]])
upper=np.array([[124],[255],[255]])
#使用cv2.inRange()函数筛选出蓝色像素
mask=cv2.inRange(imgHSV,lower,upper)
cv2.imshow("Mask",mask)
img[mask>0]=(0,0,255)
cv2.imshow("Output",img)
cv2.waitKey()
cv2.destroyAllWindows()


