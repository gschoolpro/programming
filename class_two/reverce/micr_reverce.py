# -*- coding: utf-8 -*-
#オセロ盤を作るプログラム(手動)
from mcpi import minecraft

mc = minecraft.Minecraft.create()
def set_board():
    x,y,z = mc.player.getPos()
    a=0
    b=0
    x = x + 5
    while a<8:    
        while b<8:
            if (a+b)%2==0:
                if (a==3 and b==3) or (a==4 and b==4):
                    set_white(x+a,y,z+b)
                else:
                    set_lime(x+a,y,z+b)
            elif (a+b)%2==1:
                if (a==3 and b==4) or (a==4 and b==3):
                    set_black(x+a,y,z+b)
                else:
                    set_green(x+a,y,z+b)
            b+=1
        a+=1
        b=0
    game()



def game():
    tern = 0
    while True:
        for hitBlock in mc.events.pollBlockHits():
            blockId,data = mc.getBlockWithData(hitBlock.pos.x,hitBlock.pos.y,hitBlock.pos.z)
            
            flag = check(hitBlock)
            if flag != 0:
                if blockId == 35 and (data == 13 or data == 5):
                    if tern%2 == 0:
                        set_black(hitBlock.pos.x,hitBlock.pos.y,hitBlock.pos.z)
                    elif tern%2 == 1:
                        set_white(hitBlock.pos.x,hitBlock.pos.y,hitBlock.pos.z)
                    tern += 1

                elif blockId == 35 and data == 0:
                    set_black(hitBlock.pos.x,hitBlock.pos.y,hitBlock.pos.z)
            
                elif blockId == 35 and data == 15:
                    set_white(hitBlock.pos.x,hitBlock.pos.y,hitBlock.pos.z)
            check(hitBlock)

def check(hitBlock):
    i = -1
    j = -1
    flag = 0
    while i <= 1:
        while j <= 1:
            blockId,data = mc.getBlockWithData(hitBlock.pos.x+i,hitBlock.pos.y,hitBlock.pos.z+j)
            if blockId == 35 and (data == 0 or data == 15):
                flag += 1
            j += 1
        i += 1
        j = -1
    return flag


def auto(blockId,data,hitBlock): #使ってない
    if blockId==35 and data==0:
        i=1
        while blockId != 35:
            xblockId,xdata = mc.getBlockWithData(hitBlock.pos.x+i,hitBlock.pos.y,hitBlock.pos.z)
            if xdata == 13 or xdata == 5:
                break
            if xdata == 15:
                while i>1:
                    mc.setBlock(hitBlock.pos.x+i,hitBlock.pos.y,hitBlock.pos.z,35,0)
                    i-=1
            i+=1
        while blockId != 35:
            xblockId,xdata = mc.getBlockWithData(hitBlock.pos.x+i,hitBlock.pos.y,hitBlock.pos.z)
            if xdata == 13 or xdata == 5:
                break
            if xdata == 15:
                while i>1:
                    mc.setBlock(hitBlock.pos.x-i,hitBlock.pos.y,hitBlock.pos.z,35,0)
                    i-=1
            i+=1

def set_black(x,y,z):
    mc.setBlock(x,y,z,35,15)
def set_white(x,y,z):
    mc.setBlock(x,y,z,35,0)
def set_lime(x,y,z):
    mc.setBlock(x,y,z,35,5)
def set_green(x,y,z):
    mc.setBlock(x,y,z,35,13)


if __name__ == '__main__':
    try: #通常時
        set_board()
    except KeyboardInterrupt: #キーボードが押されたとき
        pass
    finally: #終了時(Ctrl+cなど)
        pass
#    y=1
#    z=0
#    while z<=40:
#        mc.setBlock(x,y,z,1)  #目の前に石ブロックを置く
#        z+=1
#        if x==0 or z==0 or x==40 or z==40:
#            while y<=30:
#                mc.setBlock(x,y,z,3)
#                y+=1

