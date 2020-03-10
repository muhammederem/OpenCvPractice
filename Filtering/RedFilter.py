import cv2
import numpy as np

red=cv2.imread("redDetailed.jpg")
hsv=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)

red_low=np.array([155,50,50])
red_high=np.array([200,255,255])
mask=cv2.inRange(hsv,red_low,red_high)
filtered=cv2.bitwise_and(red,red,mask=mask)

cv2.imshow("mask",mask)
cv2.imshow("Lena",red)
cv2.imshow("filtered",filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()