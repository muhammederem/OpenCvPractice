import cv2
import numpy as np

yellow=cv2.imread("yellowDetailed.jpg")
hsv=cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)

white_low=np.array([5,100,100])
white_high=np.array([25,255,255])
mask=cv2.inRange(hsv,white_low,white_high)
filtered=cv2.bitwise_and(yellow,yellow,mask=mask)

cv2.imshow("mask",mask)
cv2.imshow("Original",yellow)
cv2.imshow("filtered",filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()