import cv2
import numpy as np
def mesen(image,height,width):
    cv2.rectangle(image,(100,330),(220,365),(0,0,0),thickness=-1)
    return image

image = cv2.imread('./hannin.png',-1)
height = image.shape[0] 
width = image.shape[1]
image[np.where((image[0:height,0:width,3] == 0))] = [255,255,255,255] 
image = mesen(image,height,width)
cv2.imshow('mesen',image)
cv2.waitKey()
cv2.imwrite('mesen.png',image)
