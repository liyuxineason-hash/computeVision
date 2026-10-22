import cv2
image1=cv2.imread("../photo/monkey.jpg")
image1 = cv2.resize(image1,None,fx=0.5,fy=0.5)
cv2.imshow("Monkey",image1)
image2=cv2.imread("../photo/cloud.jpg")

cv2.imshow("Cloud",image2)
rows,colmns,channel=image1.shape
image2=cv2.resize(image2,(colmns,rows))
result=cv2.addWeighted(image1,0.6,image2,0.6,0)  #进行加权加法运算
cv2.imshow("Man+Cloud",result)
cv2.waitKey()
cv2.destroyAllWindows()			     #释放所有窗口
