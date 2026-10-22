import cv2				         #导入OpenCV库
import numpy as np			          #导入NumPy库
img=cv2.imread("../photo/school.jpg")		         #读取图像
cv2.imshow("Input",img)			         #显示原图像
#将图像的色彩空间从BGR转换为HSV
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#下界数组和上界数组
lower=np.array([[100],[43],[46]])
upper=np.array([[124],[255],[255]])
#调用cv2.inRange()函数筛选出 色像素
dst=cv2.inRange(imgHSV,lower,upper)
cv2.imshow("Output",dst)			            #显示输出图像
cv2.waitKey()				            #窗口等待，按任意键继续
cv2.destroyAllWindows()			      #释放所有窗口
