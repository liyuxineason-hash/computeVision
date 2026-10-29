import cv2							#导入OpenCV库
image=cv2.imread("../material/list/dog.png")		#读取图像
cv2.imshow("Input",image)		#显示原图像
mblur = cv2.medianBlur(image, 5)	#进行中值滤波
cv2.imshow("medianBlur", mblur)	#显示中值滤波后图像
cv2.waitKey()			#按任意键继续
cv2.destroyAllWindows()		#释放所有窗口

# 中值滤波用一个像素点周围邻域内所有像素值的"中位数"，来代替该像素点原来的值。