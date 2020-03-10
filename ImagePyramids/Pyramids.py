import cv2

img=cv2.imread("lena.jpg")
cv2.imshow("Orijinal",img)

pyr_up=cv2.pyrUp(img)
cv2.imshow("Up",pyr_up)

pyr_down=cv2.pyrDown(img)
cv2.imshow("Down",pyr_down)

cv2.waitKey(0)
cv2.destroyAllWindows()