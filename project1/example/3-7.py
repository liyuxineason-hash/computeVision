import cv2						#导入OpenCV库
import numpy as np					#导入NumPy库
image=cv2.imread("../photo/school.jpg")		                          #读取图像
cv2.imshow("Input",image)			             #显示原图像
#产生与原图像形状相同且值全为100的数组
mask=np.ones(image.shape,dtype=np.uint8)*100
result1=image+mask					#使用加法运算符完成加法运算
result2=cv2.add(image,mask)	                                       #使用函数完成加法运算
cv2.imshow("Symbol",result1)	                                       #显示运算符计算结果图像
cv2.imshow("Function",result2)                                        #显示函数计算结果图像
cv2.waitKey()		                                                    #窗口等待，按任意键继续
cv2.destroyAllWindows()