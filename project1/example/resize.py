import cv2
school = cv2.imread("../photo/school.jpg")
dst =  cv2.resize(school,None,fx=1/3,fy=1/3)
dst1 =  cv2.resize(school,None,fx=2,fy=2)
cv2.imshow("school",school)
cv2.imshow("school1",dst)
cv2.imshow("school2",dst1)
k = cv2.waitKey()
if k == ord('d'):

     cv2.destroyAllWindows()
