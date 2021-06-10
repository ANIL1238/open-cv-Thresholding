import cv2
import numpy
img  = cv2.imread('imges//dhoni2.png')
retval, threshold = cv2.threshold(img, 62, 255, cv2.THRESH_BINARY)
cv2.imshow("Original Image", img)
print(img.shape)
wid,heig=400,400
imgre=cv2.resize(img,(wid,heig))
print(imgre)
threshold.resize(wid,heig)
cv2.imshow("Threshold",imgre)
cv2.waitKey(0)