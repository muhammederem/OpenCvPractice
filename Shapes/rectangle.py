import cv2
img_Lena=cv2.imread("lena.jpg")
cv2.imshow("Lena",img_Lena)

cv2.rectangle(img_Lena,(95,90),(145,140),(0,0,255),2)
cv2.imshow("RecLena",img_Lena)

cv2.waitKey(0)
cv2.destroyAllWindows()