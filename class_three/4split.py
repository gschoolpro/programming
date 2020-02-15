import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
height,width = image.shape[:2]
kirinuki1 = image[0:height/2,0:width/2]
kirinuki2 = image[0:height/2,width/2:width]
kirinuki3 = image[height/2:height,0:width/2]
kirinuki4 = image[height/2:height,width/2:width]
kirinuki1 = cv2.flip(kirinuki1,-1)
kirinuki2 = cv2.flip(kirinuki2,-1)
kirinuki3 = cv2.flip(kirinuki3,-1)
kirinuki4 = cv2.flip(kirinuki4,-1)
image[0:height/2,0:width/2] = kirinuki1
image[0:height/2,width/2:width] = kirinuki2
image[height/2:height,0:width/2] = kirinuki3
image[height/2:height,width/2:width] = kirinuki4
image = image[:,:,[2,1,0]]
plt.imshow(image)
plt.show()
plt.imsave('reverse.png',image)
