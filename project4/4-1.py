import matplotlib
matplotlib.use('TkAgg')   # 必须放在 import pyplot 之前
import cv2		#导入OpenCV库
import matplotlib.pyplot as plt	#导入Matplotlib库
image=cv2.imread("../material/list/lake.jpg")		#读取图像
#统计图像直方图信息
hist=cv2.calcHist([image],[0],None,[256],[0,255])
plt.plot(hist)              #绘制图形
plt.show()                  #显示图形


