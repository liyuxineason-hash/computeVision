import cv2											#导入程序所需的库
import numpy as np
image=np.zeros((260,550,3),dtype="uint8")+255	#创建一幅白色画布
font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX				#定义字体类型
#绘制文本
cv2.putText(image,'江西科技师范大学',(50,100),font,2,(0,0,0), 2,8)
cv2.putText(image,'江西科技师范大学',(50,155),font,2,(0,0,0), 2,8,True)
cv2.imshow('Image', image)			#显示图像
cv2.waitKey()						#窗口等待，按任意键继续
cv2.destroyAllWindows()			#释放所有窗口