import cv2 as a
import numpy as num
import tkinter as m

from matplotlib import pyplot as plt

#imageFileName = raw_input("enter the name of the image file: ")
img=a.imread('imges//dhoniface.png',0)
#tt=(img,127,255)
#tt=("Original Image", img)
ret,threst1=a.threshold(img,127,255,a.THRESH_BINARY)
ret,threst2=a.threshold(img,127,255,a.THRESH_BINARY_INV)
ret,threst3=a.threshold(img,127,255,a.THRESH_TRUNC)
ret,thres4=a.threshold(img,127,255,a.THRESH_TOZERO)
ret,threst5=a.threshold(img,127,255,a.THRESH_TOZERO_INV)
titles=['original image','binary','binary_inv','trunc','tozero','tozero_inv']
images=[img,threst1,threst2,threst3,thres4,threst5]
for i in range(6):
    a="a"
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()






