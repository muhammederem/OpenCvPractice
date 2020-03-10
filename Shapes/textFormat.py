import cv2
import numpy as np

def writeText():
    img=np.zeros((400,600,3),np.uint8)
    img.fill(0)

    fontScale=1.0
    color=(255,0,255)

    fontFace=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,"FONT_HERSHEY_COMPLEX",(10,40),fontFace,fontScale,color)

    fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(img,"FONT_HERSHEY_COMPLEX_SMALL",(10,80),fontFace,fontScale,color)

    fontFace=cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img,"FONT_HERSHEY_DUPLEX",(10,120),fontFace,fontScale,color)

    fontFace=cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img,"FONT_HERSHEY_PLAIN",(10,160),fontFace,fontScale,color)

    fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(img,"FONT_HERSHEY_SCRIPT_COMPLEX",(10,200),fontFace,fontScale,color)

    fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(img,"FONT_HERSHEY_SCRIPT_SIMPLEX",(10,240),fontFace,fontScale,color)

    fontFace=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,"FONT_HERSHEY_SIMPLEX",(10,280),fontFace,fontScale,color)

    fontFace=cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(img,"FONT_HERSHEY_TRIPLEX",(10,320),fontFace,fontScale,color)

    fontFace=cv2.FONT_ITALIC
    cv2.putText(img,"FONT_ITALIC",(10,360),fontFace,fontScale,color)

    cv2.imshow("Text",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("Fonts.jpg",img)

def main():
    writeText()

if __name__ == '__main__':
    main()
