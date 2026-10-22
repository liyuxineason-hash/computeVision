import cv2 #导入cv2库
school = cv2.imread("../photo/school.jpg") #读取图像并存储
school = cv2.resize(school,None,fx=1/2,fy=1/2) #缩小图片大小
dst1 = cv2.flip(school,1) #沿y轴翻转
# dst2 = cv2.flip(school,0)
# dst3 = cv2.flip(school,-1)
cv2.imshow("school",school)
cv2.imshow("dst1",dst1)
# cv2.imshow("dst2",dst2)
# cv2.imshow("dst3",dst3)
k = cv2.waitKey()
if k == ord('d'):
     cv2.destroyAllWindows()
