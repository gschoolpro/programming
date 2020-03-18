# -*- coding: utf-8 -*-
import cv2
# 画像読み込み
image = cv2.imread('./capture.jpg',-1)
# 縦横の長さの取得
height = image.shape[0] 
width = image.shape[1]
# 画像の上半分に紫色のフィルタを反映させる
image[0:height/2,:,0] = 255
image[0:height/2,:,2] = 255
# 画像縮小(画像が大きいとき用)
img = cv2.resize(image,(int(image.shape[1]*0.5),int(image.shape[0]*0.5)))
# 画像表示
cv2.imshow('img',img)
cv2.waitKey()
# 画像保存
cv2.imwrite('purple.png',img)
