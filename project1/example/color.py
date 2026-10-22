import cv2
imageColor = cv2.imread("../photo/school.jpg")
print("show彩色图像的属性：")
print("shape =",imageColor.shape)
print("size =",imageColor.size)
print("dtype =",imageColor.dtype)
# 灰度模式读取图像
imageGray = cv2.imread("../photo/school.jpg", 0)
print("显示灰度图像的属性：")
print("shape =",imageGray.shape)
print("size =",imageGray.size)
print("dtype =",imageGray.dtype)