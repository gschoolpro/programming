import cv2
import matplotlib.pyplot as plt
image = cv2.imread('./capture.jpg',0)
ret,img = cv2.threshold(image,150,255,cv2.THRESH_BINARY)
#plt.imshow(img)
#plt.show()
img = cv2.resize(img,(int(img.shape[1]*0.5),int(img.shape[0]*0.5)))
cv2.imshow('img',img)
cv2.waitKey()
cv2.imwrite('thresh.png',img)
