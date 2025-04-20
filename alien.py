import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface
from settings import Settings


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()

        # 获取主界面
        self.screen: Surface = game.screen
        self.screen_rect = self.screen.get_rect()

        # 加载外星人配置
        self.img = pygame.image.load(Settings.ALIEN_IMG)
        self.rect = self.img.get_rect()

        # 每个外星人一开始都在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        """ 更新外星人的位置 """
        self.x += Settings.ALIEN_SPEED * Settings.ALIEN_FLEET_DIRECTION
        self.rect.x = self.x

    def drop(self):
        """ 让外星人下落 """
        self.y += Settings.ALIEN_HEIGHT
        self.rect.y = self.y

    def check_edges(self):
        """ 判断外星人是否碰到了边界 """
        return self.rect.left <= self.screen_rect.left or self.rect.right >= self.screen_rect.right

    def blitme(self):
        """ 在screen上绘制外星人 """
        self.screen.blit(self.img, self.rect)