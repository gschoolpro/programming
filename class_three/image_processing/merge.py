# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
# 画像の読み込み
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
# 縦横の長さの取得
height,width = image.shape[:2]
# 図形・文字の貼り付け
cv2.rectangle(image,(30,60),(420,360),(255,100,100),thickness=5)
cv2.circle(image,(400,400),100,(255,0,0),thickness=5)
cv2.putText(image,"this is a sample picture.",(300,700),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),thickness=3)
# 画像の表示
plt.imshow(image)
plt.show()
# 画像の保存
plt.imsave('image_in_rectangle.png',image)
