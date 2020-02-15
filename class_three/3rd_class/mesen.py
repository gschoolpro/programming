import cv2
import numpy as np
def mesen(image,height,width):
    cv2.rectangle(image,(100,30),(160,50),(0,0,0),thickness=-1)
    image = cv2.resize(image,(int(width),int(height)))
    return image

image = cv2.imread('../gschool.jpeg',cv2.IMREAD_COLOR)
height = image.shape[0] 
width = image.shape[1]
image = mesen(image,height,width)
cv2.imshow('mesen',image)
cv2.waitKey()
cv2.imwrite('mesen.png',image)
