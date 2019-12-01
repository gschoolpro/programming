import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
image[:,:,0]=255
plt.imshow(image)
plt.show()
plt.imsave('red_filter.png',image)
