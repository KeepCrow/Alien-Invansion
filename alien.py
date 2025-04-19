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
        pass

    def blitme(self):
        self.screen.blit(self.img, self.rect)