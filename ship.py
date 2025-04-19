import pygame
from pygame.surface import Surface
from settings import Settings


class Ship:
    def __init__(self, game):
        # 获取屏幕信息
        self.screen: Surface = game.screen
        self.screen_rect = self.screen.get_rect()

        # 加载图片
        self.img = pygame.image.load(Settings.SHIP_IMG)
        self.rect = self.img.get_rect()

        # 将图片放在默认位置：屏幕底部中央
        self.rect.midright = self.screen_rect.midright

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ 根据移动标志，调整飞船位置 """
        if self.moving_up and self.rect.top > self.screen_rect.top:
            print('Ship move up')
            self.rect.y -= Settings.SHIP_SPEED
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            print('Ship move down')
            self.rect.y += Settings.SHIP_SPEED

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.img, self.rect)
