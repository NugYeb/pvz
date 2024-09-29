import os
os.chdir(os.path.dirname(__file__))

import pygame
import sys
from pygame.locals import *
import Image
import math

pygame.init()
temp1 = 0

DS_siz = (math.ceil(1280/1.2), math.ceil(720/1.2))
DS = pygame.display.set_mode(DS_siz)
BGI_siz = DS_siz
BGI_pos = (0, 0)
BGI = Image.IMAGE("..//pic/vhigbbjj.jpg", 0, 0, BGI_siz, BGI_pos)

while True:
    for EVENT in pygame.event.get():
        if EVENT.type == QUIT:
            pygame.quit()
            sys.exit()
    
    DS.fill( (0, 100, 0) )
    BGI.draw(DS)

    pygame.display.update()
