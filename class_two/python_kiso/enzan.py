#!/usr/bin/env python
# -*- coding: utf-8 -*-

# x を 5 、 y を 2 とする
x = 5
y = 2
print('x = ', x, ', y = ', y)
print ('----------------------------')

#  ----- 計算 -----
# (1-1)足し算
print('x + y =              ', x + y)
# (1-2)引き算
print('x - y =              ', x - y)
# (1-3)掛け算
print('x * y =              ', x * y)
# (1-4)割り算
print('x / y =              ', x / y)
# (1-5)割り算の余り
print('x % y =              ', x % y, '\n')

# ----- 比較 -----
# (2-1)等しいかどうか
print('x == y :             ', x == y)
# (2-2)等しくないかどうか
print('x != y :             ', x != y)
# (2-3) x は y より小さいかどうか
print('x < y :              ', x < y)
# (2-4) x は y 以下かどうか
print('x <= y :             ', x <= y)
# (2-5)x は y より大きいかどうか
print('x > y :              ', x > y)
# (2-6)x は y 以上かどうか
print('x >= y :             ', x >= y, '\n')

# ----- ブール演算子 -----
# (3-1) どちらも満たしているかどうか
print('x == 5 and y == 2 :  ', x == 5 and y == 2)
print('x == 5 and y != 2 :  ', x == 5 and y == 2)
# (3-2) どちらかを満たしているかどうか
print('x == 4 or y == 2 :   ', x == 4 or y == 2)
print('x == 4 or y == 1 :   ', x == 4 or y == 1)
# (3-1) 正しくないかどうか
print('not x == 5 :         ', not x == 5)
print('not y == 5 :         ', not y == 5)
