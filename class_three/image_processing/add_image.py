import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
#kirin = cv2.imread('./gschool.jpeg',cv2.IMREAD_COLOR)
kirin = cv2.imread('../3rd_class/hannin.png',cv2.IMREAD_COLOR)
kirin = kirin[:,:,[2,1,0]]
height,width = kirin.shape[:2]
image[100:height + 100, 200:width + 200] = kirin
plt.imshow(image)
plt.show()
#plt.imsave('image_in_image.png',image)
