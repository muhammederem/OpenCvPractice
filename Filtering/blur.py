import cv2
import numpy as np

img=cv2.imread("lena.jpg")


kernel=np.ones((15,15),np.float32)/255
smoothed=cv2.filter2D(img,-3,kernel)
gaussian=cv2.GaussianBlur(img,(15,15),1)
median=cv2.medianBlur(img,5)
biLiteral=cv2.bilateralFilter(img,15,75,75)
cv2.imshow("Lena",img)
cv2.imshow("Smoothed",smoothed)
cv2.imshow("Biliteral",biLiteral)
cv2.imshow("Median",median)
cv2.imshow("Gaussian",gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
