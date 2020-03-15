# -*- coding: utf-8 -*-
from mcpi import minecraft

mc = minecraft.Minecraft.create()  # マインクラフトに接続

mc.postToChat("Hello world")


pos = mc.player.getPos()
mc.postToChat(pos)
