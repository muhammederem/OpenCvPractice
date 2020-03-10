import cv2
import numpy as np
img=cv2.imread("text.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY_INV)

gaus=cv2.adaptiveThreshold(img,220,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,33,1)

cv2.imshow("img",img)
cv2.imshow("threshold",threshold)
cv2.imshow("gaus",gaus)
cv2.imwrite("../ImageProcess/gaus.jpg", gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()