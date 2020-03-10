import cv2
import numpy as np

lena=cv2.imread("lena.jpg")
canny=cv2.Canny(lena,100,150)

cv2.imshow("Lena",lena)
cv2.imshow("Canny",canny)


cv2.waitKey(0)
cv2.destroyAllWindows()