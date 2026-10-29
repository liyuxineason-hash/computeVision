import cv2							#导入OpenCV库
image=cv2.imread("../material/list/dog.png")		#读取图像
cv2.imshow("Input",image)			#显示原图像
blur = cv2.blur(image, (5, 5))	#进行均值滤波，滤波模板大小为(5,5)
cv2.imshow("blur ", blur)   #显示均值滤波后图像
cv2.waitKey()						#按任意键继续
cv2.destroyAllWindows()			#释放所`有窗口


# 均值滤波：在图像上滑动一个小窗口，把窗口内所有像素的平均值作为新像素值，从而达到“抹平”噪声、平滑图像的目的