import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
height,width = image.shape[:2]

cv2.rectangle(image,(30,60),(420,360),(255,100,100),thickness=5)
cv2.circle(image,(400,400),100,(255,0,0),thickness=5)
cv2.putText(image,"this is a sample picture.",(300,700),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),thickness=3)
plt.imshow(image)
plt.show()
plt.imsave('image_in_rectangle.png',image)
