import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
height,width = image.shape[:2]
kirinuki = image[100:500,200:700]
kirinuki = cv2.flip(kirinuki,1)
image[100:500,200:700] = kirinuki
image = image[:,:,[2,1,0]]
plt.imshow(image)
plt.show()
plt.imsave('reverse.png',image)
