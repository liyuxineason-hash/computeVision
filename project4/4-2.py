import matplotlib
matplotlib.use('TkAgg')   # 必须放在 import pyplot 之前
import cv2								#导入OpenCV库
import matplotlib.pyplot as plt		#导入Matplotlib库
image=cv2.imread("../material/list/flower.png")		#读取图像
#统计图像直方图信息
hist0=cv2.calcHist([image],[0],None,[256],[0,255])
hist1=cv2.calcHist([image],[1],None,[256],[0,255])
hist2=cv2.calcHist([image],[2],None,[256],[0,255])
plt.plot(hist0,color='b',linestyle='-')				#绘制图形
plt.plot(hist1,color='g',linestyle=':')
plt.plot(hist2,color='r',linestyle='-.')
plt.show()								#显示图形

