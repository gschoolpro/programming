# coding: utf-8
import cv2
import numpy as np
def bokasi(image,height,width):
 img=image.copy()
 for w in range(3,width-4):
  for h in range(3,height-4):
   image[h,w,0] = np.sum(image[h-2:h+2,w-2:w+2,0])/16
   image[h,w,1] = np.sum(image[h-2:h+2,w-2:w+2,1])/16
   image[h,w,2] = np.sum(image[h-2:h+2,w-2:w+2,2])/16
 #円状の型を作る
 mask = np.full((height,width,1),0,dtype=np.uint8)
 cv2.rectangle(mask,(110,290),(230,390),(255),-1)
 #元の画像の円の部分以外を切り抜き
 mask_inv = cv2.bitwise_not(mask)
 img1 = cv2.bitwise_and(img,img,mask=mask_inv)
 #ぼかした画像の円の部分を切り抜き
 img = cv2.bitwise_and(image,image,mask=mask)
 #切り抜いた２つの画像を合成
 image = cv2.add(img1,img)

 cv2.rectangle(image,(110,290),(230,390),(0,255,0,255)) 
 return image

image = cv2.imread('./hannin.png',-1)
height = image.shape[0] 
width = image.shape[1]
image[np.where((image[0:height,0:width,3] == 0))] = [255,255,255,255] 
image = bokasi(image,height,width)
cv2.imshow('bokasi',image)
cv2.waitKey()
cv2.imwrite('sikaku_bokasi.png',image)
