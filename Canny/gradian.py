import cv2
import numpy as np

lena=cv2.imread("lena.jpg")

laplacian=cv2.Laplacian(lena,cv2.CV_8U)
sobelX=cv2.Sobel(lena,cv2.CV_64F,1,0,ksize=5)
sobelY=cv2.Sobel(lena,cv2.CV_64F,0,1,ksize=5)


cv2.imshow("Lena",lena)
cv2.imshow("Laplacian",laplacian)
cv2.imshow("SobelX",sobelX)
cv2.imshow("SobelY",sobelY)

cv2.waitKey(0)
cv2.destroyAllWindows()