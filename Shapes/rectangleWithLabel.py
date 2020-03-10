import cv2
img_Lena=cv2.imread("lena.jpg")
cv2.imshow("Lena",img_Lena)

cv2.rectangle(img_Lena,(95,90),(145,140),(0,0,255),2)
cv2.putText(img_Lena,"Lena",(95,150),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(210,0,0),1,cv2.LINE_4) #Put text to bottom left
cv2.imshow("RecLena",img_Lena)


cv2.waitKey(0)
cv2.destroyAllWindows()