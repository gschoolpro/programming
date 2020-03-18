# -*- coding: utf-8 -*-
#画像を4つに分け、それぞれを上下反転させるプログラム
import cv2
import numpy as np
import matplotlib.pyplot as plt
# 画像読み込み
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
# 縦横の長さの取得
height,width = image.shape[:2]

# 画像を４つに分ける
kirinuki1 = image[0:height/2,0:width/2]
kirinuki2 = image[0:height/2,width/2:width]
kirinuki3 = image[height/2:height,0:width/2]
kirinuki4 = image[height/2:height,width/2:width]
# 画像反転( = 0:上下反転, > 0:左右反転, < 0:上下左右反転)
kirinuki1 = cv2.flip(kirinuki1,-1)
kirinuki2 = cv2.flip(kirinuki2,-1)
kirinuki3 = cv2.flip(kirinuki3,-1)
kirinuki4 = cv2.flip(kirinuki4,-1)
# 反転後の画像を適用
image[0:height/2,0:width/2] = kirinuki1
image[0:height/2,width/2:width] = kirinuki2
image[height/2:height,0:width/2] = kirinuki3
image[height/2:height,width/2:width] = kirinuki4
# 色の補正
image = image[:,:,[2,1,0]]
# 画像の表示
plt.imshow(image)
plt.show()
# 画像の保存
plt.imsave('reverse.png',image)
