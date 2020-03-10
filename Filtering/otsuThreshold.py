import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('rontgen.jpg',0)

_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur=cv2.GaussianBlur(img,(5,5),0)
_,th3=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

images=[img,0,th1,
          img,0,th2,
          blur,0,th3]
names=['orjinal','Histogram','Thresholding(127)',
           'orjinal', 'Histogram','Otsu Thresholding',
            'Gaussian Blur', 'Histogram', 'Otsu Thresholding']

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(names[i*3]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(names[i*3+1]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(names[i*3+2]),plt.xticks([]),plt.yticks([])

plt.show()