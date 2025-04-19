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
        self.rect.midbottom = self.screen_rect.midbottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ 根据移动标志，调整飞船位置 """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += Settings.SHIP_SPEED
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= Settings.SHIP_SPEED

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.img, self.rect)
