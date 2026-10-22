import cv2					             #导入OpenCV库
import numpy as np				             #导入NumPy库
image=cv2.imread("../photo/monkey&beauty.jpg")
image=cv2.resize(image,None,fx=0.5,fy=0.5)#读取原图像
cv2.imshow("Input",image)				#显示原图像
#产生与原图像形状相同且值全为0的掩模
mask=np.zeros(image.shape,dtype=np.uint8)
mask[300:500,100:400,]=255 			             #在掩模上设置白色中间区域
cv2.imshow("Mask",mask)				#显示掩模
result=cv2.bitwise_and(image,mask)	                          #进行按位与运算
cv2.imshow("Result",result)			             #显示加上掩模后的图像
cv2.waitKey()					             #窗口等待，按任意键继续
cv2.destroyAllWindows()