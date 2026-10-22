import cv2
img = cv2.imread("../photo/school.jpg")  # 读取图像
cv2.imshow("Input",img)	#显示原图
rows = len(img)    #行数
cols = len(img[0]) #列数
center = (rows / 2, cols / 2)  # 图像中心点
# 对图像进行旋转
M = cv2.getRotationMatrix2D(center, 330, 1)
dst = cv2.warpAffine(img, M, (cols, rows))  # 按照M进行仿射
# 沿着x进行翻转
dst1 = cv2.flip(dst, 0)
cv2.imwrite('save_flower.jpg', dst1)# 保存图像到当前路径
cv2.imshow("Output",dst1)					#显示旋转后的图像
cv2.waitKey()								#窗口等待，按任意键继续
cv2.destroyAllWindows()					#释放所有窗口