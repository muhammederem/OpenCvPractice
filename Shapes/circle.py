import cv2
import numpy as np

img=np.zeros((150,150,3),dtype="uint8")
#Create an black blank image

cv2.rectangle(img,(10,10),(140,140),(250,250,0),5) #Rectangle
cv2.circle(img,(75,75),50,(0,250,250),5) #Circle

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()