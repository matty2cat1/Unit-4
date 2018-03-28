#Matt Westelman
#3/28/18
#colorChangeWindow.py
from random import randint
from ggame import *
green = Color(0x006600,1)
brown = Color(0x8B4513,1)
yellow = Color(0xFFFF00,1)

def mouseClick(event):
    color = randint(1,3)
    if color == 1:
        rekt = RectangleAsset(500,500, LineStyle(1,green),green)
    elif color == 2:
        rekt = RectangleAsset(500,500, LineStyle(1,brown),brown)
    else:
        rekt = RectangleAsset(500,500, LineStyle(1,yellow),yellow)

    Sprite(rekt)
App().listenMouseEvent('click', mouseClick)
App().run()
