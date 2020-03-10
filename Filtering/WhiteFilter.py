import cv2
import numpy as np

white=cv2.imread("redDetailed.jpg")
hsv=cv2.cvtColor(white,cv2.COLOR_BGR2HSV)

white_low=np.array([0 ,0,140])
white_high=np.array([256,60,255])
mask=cv2.inRange(hsv,white_low,white_high)
filtered=cv2.bitwise_and(white,white,mask=mask)

cv2.imshow("mask",mask)
cv2.imshow("Original",white)
cv2.imshow("filtered",filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()