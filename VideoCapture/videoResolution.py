import cv2

camera=cv2.VideoCapture("sample.mp4")#For Web Cam; Change parameter with 0

def resolution(x,y):
    camera.set(3,x)
    camera.set(4,y)

def scale(frame,percent):
    height=int(frame.shape[0]*percent/100)
    width=int(frame.shape[1]*percent/100)
    dim=(width,height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)



#resolution(640, 480)
while True:
    ret,frame=camera.read()
    frame75=scale(frame,75)
    frame150=scale(frame,150)
    cv2.imshow("Frame75", frame75)
    cv2.imshow("Frame150",frame150)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(30) & 0xFF==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()