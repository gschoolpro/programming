# -*- coding utf-8 -*-
import cv2
import numpy as np
# 画像読み込み
image = cv2.imread('./capture.jpg',-1)
# 縦横の長さ取得
height = image.shape[0] 
width = image.shape[1]
# 反転用の空画像
tmp = np.empty((height,width,3))
for x in range(width/2):  # 画像反転(x方向)
    tmp[:,x] = image[:,x]
    image[:,x] = image[:,width-x-1]
    image[:,width-x-1] = tmp[:,x]
# 画像縮小(画像が大きいとき用)
img = cv2.resize(image,(int(width*0.5),int(height*0.5)))
# 画像表示
cv2.imshow('img',img)
cv2.waitKey()
# 画像保存
cv2.imwrite('hanten.png',image)
