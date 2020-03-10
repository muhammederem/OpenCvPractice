import cv2
import numpy as np

blue=cv2.imread("blueDetailed.jpg")
hsv=cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)

blue_low=np.array([60,60,60])
blue_high=np.array([140,255,255])
mask=cv2.inRange(hsv,blue_low,blue_high)
filtered=cv2.bitwise_and(blue,blue,mask=mask)

cv2.imshow("mask",mask)
cv2.imshow("Original",blue)
cv2.imshow("filtered",filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()