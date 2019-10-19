# -*- coding: utf-8 -*-
from mcpi import minecraft

mc = minecraft.Minecraft.create()

x,y,z = mc.player.getPos()
i=0
j=0

while i<10:
    while j<10:
        mc.setBlock(x+1+i,y,z+j,46,1)
        j+=1
    j=0
    i+=1
while True:
    for hitBlock in mc.events.pollBlockHits():
        if mc.getBlock(hitBlock.pos.x,hitBlock.pos.y,hitBlock.pos.z) == 1:
            mc.setBlock(hitBlock.pos.x,hitBlock.pos.y,hitBlock.pos.z,2)
            break

