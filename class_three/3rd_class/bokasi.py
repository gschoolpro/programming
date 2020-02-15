import cv2
import numpy as np
def bokasi(image,height,width):
    for n in range(3):
        for w in range(3,width-4):
            for h in range(3,height-4):
                image[h,w,0] = np.sum(image[h-2:h+2,w-2:w+2,0])/16
                image[h,w,1] = np.sum(image[h-2:h+2,w-2:w+2,1])/16
                image[h,w,2] = np.sum(image[h-2:h+2,w-2:w+2,2])/16
    return image

image = cv2.imread('./hannin.png',-1)
height = image.shape[0] 
width = image.shape[1]
image[np.where((image[0:height,0:width,3] == 0))] = [255,255,255,255] 
image = bokasi(image,height,width)
cv2.imshow('bokasi',image)
cv2.waitKey()
cv2.imwrite('bokasi.png',image)
