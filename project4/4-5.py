import cv2							#导入OpenCV库
image=cv2.imread("../material/list/dog.png")		#读取图像
cv2.imshow("Input",image)			#显示原图像
blur = cv2.GaussianBlur(image, (3, 3),3)	#进行高斯滤波，滤波模板大小为(5,5)
cv2.imshow("GaussianBlur ", blur)   #显示均值滤波后图像
cv2.waitKey()						#按任意键继续
cv2.destroyAllWindows()			#释放所有窗口


# 高斯滤波：离中心点越近的像素，对结果的贡献越大；越远的像素贡献越小。