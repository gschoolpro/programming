# -*- coding: utf-8 -*-
import cv2
import numpy as np
# 画像に写っている顔の目元に画像を挿入
def mesen(image,height,width):
    cv2.rectangle(image,(100,330),(220,365),(0,0,0,255),thickness=-1)
    return image
# 画像読み込み
image = cv2.imread('./hannin.png',-1)
# 縦横の長さを取得
height = image.shape[0] 
width = image.shape[1]
# 透過背景を白色背景に変換(画素ごとの操作が行えないため)
image[np.where((image[0:height,0:width,3] == 0))] = [255,255,255,255] 
image = mesen(image,height,width)
# 画像表示
cv2.imshow('mesen',image)
cv2.waitKey()
# 画像保存
cv2.imwrite('mesen.png',image)
