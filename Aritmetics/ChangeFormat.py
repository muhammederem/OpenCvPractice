import cv2
import numpy as np

def save(path,img,jpg_Quality=None,png_compress=None):
    if jpg_Quality:
        cv2.imwrite(path,img,[int(cv2.IMWRITE_JPEG_QUALITY),jpg_Quality])
    elif png_compress:
        cv2.imwrite(path,img,[int(cv2.IMWRITE_PNG_COMPRESSION),png_compress])
    else:
        cv2.imwrite(path,img)

def main():
    imgPath="cicek.png"
    img=cv2.imread(imgPath)

    cv2.imshow('cicek',img)
    output_jpeg="cicekJPG.jpg"
    save(output_jpeg,img,jpg_Quality=85)

    output_png="cicekPNG.png"
    save(output_png,img,png_compress=4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()