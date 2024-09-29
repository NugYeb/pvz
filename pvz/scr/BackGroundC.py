import pygame
import time
import math

class BackGroundChange(pygame.sprite.Sprite):

    def __init__(self, wd_siz):
        self.wd_size = wd_siz


    def picBG(self, picPath, wd, pos=None, img_siz=None):
        self.path = picPath
        self.initImg()
        
        if img_siz != None:
            self.img = pygame.transform.scale(self.img, img_siz)
        else:
            self.img = pygame.transform.scale(self.img, self.wd_size)
        
        if pos != None:
            pos = list(pos)
            self.setPos(pos)
        
        self.draw(wd)


    def fitBG(self, picPath, wd, sign, allsign):
        self.path = picPath
        self.initImg()
        self.csiz_by_hit(self.wd_size[1])

        wid = self.img.get_size()[0]
        pos = [-(wid-self.wd_size[0])/2, 0]
        self.setPos(pos)
        
        if sign <= (allsign/30):
            # 初始位置停留
            pass
        elif sign <= (allsign/30*14):
            # 向左偏移
            pos[0] = pos[0] - (sign-(allsign/30)) * ((wid-self.wd_size[0])/2)/((allsign/30*14)-(allsign/30))
            self.setPos(pos)
        elif sign <= (allsign/30*16):
            # 停留
            pos[0] = pos[0] - ((allsign/30*14)-(allsign/30)) * ((wid-self.wd_size[0])/2)/((allsign/30*14)-(allsign/30))
            self.setPos(pos)
        elif sign <= allsign:
            # 向右偏移
            pos[0] = -(wid-self.wd_size[0]) + (sign-(allsign/30*16)) * ((wid-self.wd_size[0])/2)/((allsign)-(allsign/30*16))
            self.setPos(pos)

        self.draw(wd)
        # pygame.display.update()


    def initImg(self):
        self.img = pygame.image.load(self.path)
        self.rect = self.img.get_rect()

    
    def setPos(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]


    def csiz_by_wit(self, nwit):
        wid, hit = self.img.get_size()
        nhit = hit * nwit / wid
        self.img = pygame.transform.scale(self.img, (nwit, nhit))

    
    def csiz_by_hit(self, nhit):
        wid, hit = self.img.get_size()
        nwit = wid * nhit / hit
        self.img = pygame.transform.scale(self.img, (nwit, nhit))


    def draw(self, wd):
        wd.blit(self.img, self.rect)
