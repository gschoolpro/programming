import cv2
import numpy as np
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
height = image.shape[0] 
width = image.shape[1]
tmp = np.empty((height,width,3))
for x in range(width/2):
    tmp[:,x] = image[:,x]
    image[:,x] = image[:,width-x-1]
    image[:,width-x-1] = tmp[:,x]
img = cv2.resize(image,(int(width*0.5),int(height*0.5)))
cv2.imshow('img',img)
cv2.waitKey()
cv2.imwrite('hanten.png',image)
