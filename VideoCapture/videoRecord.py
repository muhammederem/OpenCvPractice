import cv2

cam=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
rec=cv2.VideoWriter_fourcc('Record.mp4',fourcc,20.0,(640,480))

while cam.isOpened():
    ret,video=cam.read()
    if ret==True:
        video=cv2.flip(video,0)
        rec.write(video)
        cv2.imshow("Record",video)
        video=cv2.flip(video,1)
        rec.write(video)
        cv2.imshow("Record",video)
        if cv2.waitKey(1) & 0xFF==ord('e'):
            break
    else:
        break
cam.release()
rec.release()
cv2.destroyAllWindows()