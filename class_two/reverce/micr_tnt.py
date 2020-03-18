# -*- coding: utf-8 -*-
from mcpi import minecraft

mc = minecraft.Minecraft.create()  # マインクラフトに接続

x,y,z = mc.player.getPos()  # プレイヤーの位置を取得
i=0
j=0

while i<10:
    while j<10:
        mc.setBlock(x+1+i,y,z+j,46,1)  # tntを置く
        j+=1
    j=0
    i+=1
while True:
    for hitBlock in mc.events.pollBlockHits():  # 剣で叩いたとき
        if mc.getBlock(hitBlock.pos.x,hitBlock.pos.y,hitBlock.pos.z) == 1:
            mc.setBlock(hitBlock.pos.x,hitBlock.pos.y,hitBlock.pos.z,2)
            break

