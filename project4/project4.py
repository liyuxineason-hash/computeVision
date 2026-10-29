import cv2
def onValue(obj):
    pass
image = cv2.imread('../material/list/dog.png')
cv2.imshow('Input', image)
cv2.namedWindow('MedianBlur')
cv2.createTrackbar('Value', 'MedianBlur', 0, 100, onValue)
while True:
    Value = cv2.getTrackbarPos('Value', 'MedianBlur')
    median = cv2.medianBlur(image, 2 * Value + 1)
    cv2.imshow('MedianBlur', median)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
cv2.destroyAllWindows()
