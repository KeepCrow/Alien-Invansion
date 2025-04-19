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
        self.color = Settings.BULLET_COLOR
        self.rect = pygame.Rect(0, 0, Settings.BULLET_WIDTH, Settings.BULLET_HEIGHT)
        self.rect.midtop = game.ship.rect.midtop

        self.y = self.rect.y

    def update(self):
        """ 向上移动子弹 """
        self.y -= Settings.BULLET_SPEED
        self.rect.y = self.y

    def drawme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
