import cv2							#导入程序所需的库
import numpy as np
img = np.zeros((200,220, 3), dtype="uint8")+255#创建一幅白色画布
cv2.rectangle(img,(20,10),(200,150),(255,204,0))#绘制天蓝色的矩形
#绘制上方的红色标志
cv2.ellipse(img, (106, 50), (30, 30), 120, 0, 300, (0, 0, 255), -1, cv2.LINE_AA)
cv2.circle(img, (106, 50), 10, (255, 255, 255), -1, cv2.LINE_AA)
#绘制左下角的绿色标志
cv2.ellipse(img, (76, 110), (30, 30), 0, 0, 300, (0, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (76, 110), 10, (255, 255, 255), -1, cv2.LINE_AA)
#绘制右下角的蓝色标志
cv2.ellipse(img, (140, 110), (30, 30), -60, 0, 300, (255, 0,0), -1, cv2.LINE_AA)
cv2.circle(img, (140, 110), 10, (255, 255, 255), -1, cv2.LINE_AA)
cv2.imshow('Image', img)#显示图像
cv2.waitKey()						#窗口等待，按任意键继续
cv2.destroyAllWindows()			#释放所有窗口