import cv2							#导入OpenCV库
image=cv2.imread("../material/list/dog.png")		#读取图像
cv2.imshow("Input",image)			#显示原图像
blur = cv2.blur(image, (5, 5))	#进行均值滤波，滤波模板大小为(5,5)
cv2.imshow("blur ", blur)   #显示均值滤波后图像

blur = cv2.GaussianBlur(image, (3, 3),3)	#进行高斯滤波，滤波模板大小为(5,5)
cv2.imshow("GaussianBlur ", blur)   #显示均值滤波后图像

mblur = cv2.medianBlur(image, 5)	#进行中值滤波
cv2.imshow("medianBlur", mblur)	#显示中值滤波后图像








cv2.waitKey()						#按任意键继续
cv2.destroyAllWindows()			#释放所`有窗口


