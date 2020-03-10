import cv2

camera=cv2.VideoCapture("sample.mp4")#For Web Cam; Change parameter with 0
#camera.set(cv2.CAP_PROP_FRAME_HEIGHT,100)#to Change Camera Height and Width
#camera.set(cv2.CAP_PROP_FRAME_WIDTH,100)

while True:
    ret,frame=camera.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray",gray)

    cv2.imshow("Frame",frame)
    if cv2.waitKey(30) & 0xFF==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()