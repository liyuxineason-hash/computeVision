
import cv2								#导入OpenCV库
import matplotlib.pyplot as plt		#导入Matplotlib库
image=cv2.imread("../material/list/lake.jpg")			#读取图像
cv2.imshow("Input",image)				#显示原图像
#从BGR色彩空间转换为GRAY色彩空间
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
eqHist=cv2.equalizeHist(gray)			#进行直方图均衡化
cv2.imshow("equalizeHist",eqHist)	#显示直方图均衡后的图像
plt.figure(figsize=(10,10))			#创建画布并设置画布的大小
#统计原图像直方图信息
hist1=cv2.calcHist([image],[0],None,[256],[0,255])
plt.subplot(121)							#绘制直方图
plt.title("Input")
plt.plot(hist1)
#统计直方图均衡化后的图像直方图信息
hist2=cv2.calcHist([eqHist],[0],None,[256],[0,255])
plt.subplot(122)							#绘制直方图
plt.title("equalizeHist")
plt.plot(hist2)
plt.show()								#显示图形
cv2.waitKey()							#窗口等待，按任意键继续
cv2.destroyAllWindows()				#释放所有窗口
