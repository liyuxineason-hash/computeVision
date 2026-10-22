import cv2
import numpy as np
img_path="photo/orange.jpg"
img=cv2.imread(img_path)
cv2.imshow("Original",img)				#显示原图像
#将RGB图像转换为HSV图像
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",imgHSV)
#2．创建滑动条窗口
def empty(obj):
	pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
#创建6个滑动条并添加到滑动条窗口
cv2.createTrackbar("Hue Min","TrackBars",0,180,empty)
cv2.createTrackbar("Hue Max","TrackBars",19,180,empty)
cv2.createTrackbar("Sat Min","TrackBars",134,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",160,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
#3．色彩分割
while True:
	#获取6个滑动条的值
	h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
	h_max=cv2.getTrackbarPos("Hue Max","TrackBars")
	s_min=cv2.getTrackbarPos("Sat Min","TrackBars")
	s_max=cv2.getTrackbarPos("Sat Max","TrackBars")
	v_min=cv2.getTrackbarPos("Val Min","TrackBars")
	v_max=cv2.getTrackbarPos("Val Max","TrackBars")
	#定义下界阈值数组和上界阈值数组
	lower=np.array([h_min, s_min, v_min])
	upper=np.array([h_max, s_max, v_max])
	#使用cv2.inRange()函数得到掩模图像
	mask=cv2.inRange(imgHSV,lower,upper)
	cv2.imshow("Mask",mask)				#显示掩模图像
	#原图像与原图像进行按位与运算，掩模为图像mask，得到结果图像imgResult
	imgResult=cv2.bitwise_and(img,img,mask=mask)
	cv2.imshow("Result",imgResult)	#显示结果图像
	key=cv2.waitKey(1)					#等待1毫秒并读取按键
	if key==ord('q'):					#若按'q'键，则结束循环
		break
	if cv2.getWindowProperty("TrackBars",cv2.WND_PROP_VISIBLE)<1:	#若窗口被关闭
		break
cv2.destroyAllWindows()				#释放所有窗口






