# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt
# 画像読み込み
image = cv2.imread('./capture.jpg',0)
# 2値化
ret,img = cv2.threshold(image,150,255,cv2.THRESH_BINARY)
# 画像縮小(画像が大きいとき用)
img = cv2.resize(img,(int(img.shape[1]*0.5),int(img.shape[0]*0.5)))
# 画像表示
cv2.imshow('img',img)
cv2.waitKey()
# 画像保存
cv2.imwrite('thresh.png',img)
