import cv2							#导入OpenCV库									#导入OpenCV库
image=cv2.imread("../material/list/banana.png")					#读取图像
cv2.imshow("Input",image)							#显示原图像
b_filter=cv2.bilateralFilter(image,-1,100,120)	#进行双边滤波
cv2.imshow("bilateralFilter",b_filter)		#显示双边滤波后图像
cv2.waitKey()									#按任意键继续
cv2.destroyAllWindows()						#释放所有窗口
