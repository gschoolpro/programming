# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
# 画像の読み込み
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
#kirin = cv2.imread('./gschool.jpeg',cv2.IMREAD_COLOR)
# 貼り付け画像の読み込み
kirin = cv2.imread('../3rd_class/hannin.png',cv2.IMREAD_COLOR)
# RとBの反転
kirin = kirin[:,:,[2,1,0]]
# 縦横の長さの取得
height,width = kirin.shape[:2]
# kirin(画像)の貼り付け
image[100:height + 100, 200:width + 200] = kirin
# 編集画像の表示
plt.imshow(image)
plt.show()
#plt.imsave('image_in_image.png',image)
