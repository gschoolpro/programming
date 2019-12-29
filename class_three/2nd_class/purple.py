import cv2
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
height = image.shape[0] 
width = image.shape[1]
image[0:height/2,:,0] = 255
image[0:height/2,:,2] = 255
img = cv2.resize(image,(int(image.shape[1]*0.5),int(image.shape[0]*0.5)))
cv2.imshow('img',img)
cv2.waitKey()
cv2.imwrite('purple.png',img)
