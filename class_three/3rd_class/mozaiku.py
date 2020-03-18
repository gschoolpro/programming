# -*- coding: utf-8 -*-
import cv2
import numpy as np
# 画像全体にモザイクをかける処理
def mozaiku(image,height,width):
    # 画像を縮小する
    image = cv2.resize(image,None,fx=0.1,fy=0.1)
    # 画像を元の大きさに戻す
    image = cv2.resize(image,(width,height))#,interpolation = cv2.cv.CV_INTER_NN)
    return image
# 画像読み込み
image = cv2.imread('./hannin.png',-1)
# 縦横の長さ取得
height = image.shape[0] 
width = image.shape[1]
# 透過背景を白色背景に変換
image[np.where((image[0:height,0:width,3] == 0))] = [255,255,255,255] 
image = mozaiku(image,height,width)
# 画像表示
cv2.imshow('mozaiku',image)
cv2.waitKey()
# 画像読み込み
cv2.imwrite('zaiku.png',image)
