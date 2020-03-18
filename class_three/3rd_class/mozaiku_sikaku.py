# coding: utf-8
import cv2
import numpy as np
def bokasi(image,height,width):  # 画像にモザイクを入れる関数
 img=image.copy()  # 画像をコピー
 # 画像を縮小する
 image = cv2.resize(image,None,fx=0.1,fy=0.1)
 # 画像をもとの大きさに戻す
 image = cv2.resize(image,(width,height))#,interpolation = cv2.cv.CV_INTER_NN)
 
 #四角形の型を作る
 mask = np.full((height,width,1),0,dtype=np.uint8)
 cv2.rectangle(mask,(110,290),(230,390),(255),-1)
 #元の画像の四角形部分以外を切り抜き
 mask_inv = cv2.bitwise_not(mask)
 img1 = cv2.bitwise_and(img,img,mask=mask_inv)
 #モザイク画像の四角形部分を切り抜き
 img = cv2.bitwise_and(image,image,mask=mask)
 #切り抜いた２つの画像を合成
 image = cv2.add(img1,img)
 # 画像のモザイク部分を四角形で囲う
 cv2.rectangle(image,(110,290),(230,390),(0,255,0,255)) 
 return image
# 画像の読み込み
image = cv2.imread('./hannin.png',-1)
# 縦横の長さを取得
height = image.shape[0] 
width = image.shape[1]
# 透過背景を白色背景に変換
image[np.where((image[0:height,0:width,3] == 0))] = [255,255,255,255] 
image = bokasi(image,height,width)
# 画像を表示
cv2.imshow('bokasi',image)
cv2.waitKey()
# 画像を保存
cv2.imwrite('sikaku_mozaiku.png',image)
