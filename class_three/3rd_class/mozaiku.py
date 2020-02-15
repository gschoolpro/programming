import cv2
import numpy as np
def mozaiku(image,height,width):
    image = cv2.resize(image,None,fx=0.1,fy=0.1)
    image = cv2.resize(image,(width,height))#,interpolation = cv2.cv.CV_INTER_NN)
    return image

image = cv2.imread('./hannin.png',-1)
height = image.shape[0] 
width = image.shape[1]
image[np.where((image[0:height,0:width,3] == 0))] = [255,255,255,255] 
image = mozaiku(image,height,width)
cv2.imshow('mozaiku',image)
cv2.waitKey()
cv2.imwrite('zaiku.png',image)
