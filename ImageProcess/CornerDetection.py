import cv2
import numpy as np
img=cv2.imread("corner.png")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGray=np.float32(imgGray)
corners=cv2.goodFeaturesToTrack(imgGray,135,0.0001,0)
corners=np.int0(corners)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),4,(255,0,0),-1)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
