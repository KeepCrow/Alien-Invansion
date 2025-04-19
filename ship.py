import pygame
from pygame.surface import Surface


class Ship:
    def __init__(self, game):
        # 获取屏幕信息
        self.screen: Surface = game.screen
        self.screen_rect = self.screen.get_rect()

        # 加载图片
        self.img = pygame.image.load('imgs/ship.png')
        self.rect = self.img.get_rect()

        # 将图片放在默认位置：屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.img, self.rect)
