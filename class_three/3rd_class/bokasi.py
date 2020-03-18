# -*- coding: utf-8 -*-
import cv2
import numpy as np
def bokasi(image,height,width):  # 画像にぼかしを入れる関数
    for n in range(3): 
        for w in range(3,width-4):
            for h in range(3,height-4):
                # 各RGB値それぞれにぼかす処理を入れる
                image[h,w,0] = np.sum(image[h-2:h+2,w-2:w+2,0])/16
                image[h,w,1] = np.sum(image[h-2:h+2,w-2:w+2,1])/16
                image[h,w,2] = np.sum(image[h-2:h+2,w-2:w+2,2])/16
    return image
# 画像読み込み
image = cv2.imread('./hannin.png',-1)
# 縦横の長さ取得
height = image.shape[0] 
width = image.shape[1]
# 透過部分を白背景に変換
image[np.where((image[0:height,0:width,3] == 0))] = [255,255,255,255] 
image = bokasi(image,height,width)
# 画像表示
cv2.imshow('bokasi',image)
cv2.waitKey()
# 画像出力
cv2.imwrite('bokasi.png',image)
