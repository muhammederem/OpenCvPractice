import cv2
import numpy as np

img=np.zeros((150,150,3),dtype="uint8")
#Create an black blank image

cv2.rectangle(img,(10,10),(140,140),(250,250,0),5)

cv2.line(img,(10,10),(140,140),(250,0,250),5)#Cross

cv2.line(img,(10,10),(10,140),(0,250,250),5)#Vertical

cv2.line(img,(10,10),(140,10),(255,12,45),5)#Horizantal




cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()