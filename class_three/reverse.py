# -*- coding: utf-8 -*-
#画像の一部を左右反転させるプログラム
import cv2
import numpy as np
import matplotlib.pyplot as plt
# 画像読み込み
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
# 縦横の長さの取得
height,width = image.shape[:2]
# 画像の一部を切り抜きする
kirinuki = image[100:500,200:700]
# 画像を左右反転させる
kirinuki = cv2.flip(kirinuki,1)
# 反転させた画像を元の位置に戻す
image[100:500,200:700] = kirinuki
# 色の補正
image = image[:,:,[2,1,0]]
# 画像の表示
plt.imshow(image)
plt.show()
# 画像の保存
plt.imsave('reverse.png',image)
