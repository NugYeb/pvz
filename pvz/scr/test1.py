import os
os.chdir(os.path.dirname(__file__))

import pygame
import time
import math
import sys
import gc
from pygame.locals import *
from BackGroundC import BackGroundChange as bgc

pygame.init()

# 创建窗口
wd_siz = (math.ceil(1280/1.2), math.ceil(720/1.2))
wd = pygame.display.set_mode(wd_siz)

# 创建背景
bg = bgc(wd_siz)

# 静态标题背景
picbgpath = '../pic/bmtibbjj.jpg'

# 动态战斗背景
fitbgpath = '../pic/vfdpbbjj1.jpg'
temptim1 = 0
temptim2 = 0
allsign = 300

while True:
    for EVENT in pygame.event.get():
        if EVENT.type == QUIT:
            pygame.quit()
            sys.exit()

    # bg.picBG(picPath=picbgpath, wd=wd)

    if temptim1 <= allsign:
        temptim2 += 1
        if temptim2 >= 1:
            temptim2 = 0
            temptim1 += 1
            bg.fitBG(fitbgpath, wd, temptim1, allsign)
    print(temptim1)

    gc.collect()

    pygame.display.update()
