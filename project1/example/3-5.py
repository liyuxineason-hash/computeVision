import cv2				  #导入OpenCV库
image=cv2.imread("../photo/school.jpg")                 #读取图像
cv2.imshow("BGR",image)		   #显示BGR图像
b,g,r=cv2.split(image)			   #拆分BGR图像的通道
bgr_merge=cv2.merge([b,g,r])		    #按BGR顺序合并图像
cv2.imshow("BGR_Merge",bgr_merge)	    #显示按BGR顺序合并的图像
rgb_merge=cv2.merge([r,g,b])                    #按RGB顺序合并图像
#显示按RGB顺序合并的图像
cv2.imshow("RGB_Merge",rgb_merge)
cv2.waitKey()			                #窗口等待，按任意键继续
cv2.destroyAllWindows()		   #释放所有窗口
