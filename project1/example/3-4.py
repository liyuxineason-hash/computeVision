import cv2				#导入OpenCV库
image=cv2.imread("../photo/school.jpg")		#读取图像
cv2.imshow("BGR",image)		#显示BGR图像
#将图像的色彩空间从BGR转换为HSV
hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv_image)	             #拆分HSV图像的通道
cv2.imshow("H",h)			#显示H通道的灰度图像
cv2.imshow("S",s)			#显示S通道的灰度图像
cv2.imshow("V",v)			#显示V通道的灰度图像
cv2.waitKey()				#窗口等待，按任意键继续
cv2.destroyAllWindows()	             #释放所有窗口
