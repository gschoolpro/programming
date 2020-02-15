import cv2
import numpy as np
def bokasi(image,height,width):
    for w in range(width-1):
        for h in range(height-1):
            if w > 3 and w < width-3:
                if h > 3 and h < height-3:    
                    image[h,w,0] = np.sum(image[h-2:h+2,w-2:w+2,0])/16
                    image[h,w,1] = np.sum(image[h-2:h+2,w-2:w+2,1])/16
                    image[h,w,2] = np.sum(image[h-2:h+2,w-2:w+2,2])/16
    image = cv2.resize(image,(int(width),int(height)))
    return image

image = cv2.imread('../gschool.jpeg',cv2.IMREAD_COLOR)
height = image.shape[0] 
width = image.shape[1]
image = bokasi(image,height,width)
cv2.imshow('bokasi',image)
cv2.waitKey()
cv2.imwrite('bokasi.png',image)
