import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface
from settings import Settings


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()

        # 主屏幕信息
        self.screen: Surface = game.screen
        self.screen_rect = self.screen.get_rect()

        # 加载图片
        self.img = pygame.image.load(Settings.ALIEN_IMG)
        self.rect = self.img.get_rect()
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.width // 2

    def blitme(self):
        self.screen.blit(self.img, self.rect)