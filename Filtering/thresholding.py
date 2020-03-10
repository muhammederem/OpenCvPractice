import cv2
from matplotlib import pyplot as plt
import numpy as np

img =cv2.imread("redDetailed.jpg")
ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

names=("ORIJINAL","THRESH_BINARY","THRESH_BINARY_INV","THRESH_TRUNC","THRESH_TOZERO","THRESH_TOZERO_INV")
images=(img,thresh1,thresh2,thresh3,thresh4,thresh5)

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.title(names[i])
    plt.xticks([]),plt.yticks([])
cv2.imshow("orijin",img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


