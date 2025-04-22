import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface
from settings import Settings


class Bullet(Sprite):
    """ 管理飞船所发射的所有子弹 """

    def __init__(self, game):
        super().__init__()

        # 主界面屏幕
        self.screen: Surface = game.screen
        self.screen_rect = self.screen.get_rect()

        # 创建子弹
        self.img = pygame.image.load(Settings.BULLET_IMAGE).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.midright = game.ship.rect.midleft

        self.x = self.rect.x

    def update(self):
        """ 向左移动子弹 """
        self.x -= Settings.BULLET_SPEED
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.img, self.rect)
