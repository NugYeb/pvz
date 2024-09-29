import pygame

'''
# 图片封装： import image
# img = image.IMAGE('/path')    生成加载图片
# img.draw(DS)  传入目标窗口
'''

class IMAGE(pygame.sprite.Sprite):

    def __init__(self, pathFmt, pathIndex, pathCount, size, pos):
        self.pathFmt = pathFmt
        self.pathIndex = pathIndex
        self.pathCount = pathCount
        self.size = size
        self.pos = list(pos)
        
        self.UpdataImage()


    def UpdataImage(self):
        path = self.pathFmt
        if self.pathCount != 0:
            path = path % self.pathIndex
        self.image = pygame.image.load(path)

        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)


    def UpdataSize(self, size):
        self.size = size
        self.UpdataImage()


    def UpdataIndex(self, pathIndex):
        self.pathIndex = pathIndex
        self.UpdataImage()


    def getRect(self):
        rect = self.image.get_rect()
        rect.x, rect.y = self.pos
        return rect


    def domove(self):
        self.pos[0] += 0.7
        if self.pos[0] >= 800:
            self.pos[0] = -self.size[0]

    def draw(self, DS):
        DS.blit(self.image, self.getRect())
