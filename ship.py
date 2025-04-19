import pygame
from pygame.surface import Surface


class Ship:
    def __init__(self, game):
        self.screen: Surface = game.screen
        self.screen_rect = self.screen.get_rect()

        # 加载飞船配置
        self.img = pygame.image.load('imgs/ship.png')
        self.rect = self.img.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # 移动配置
        self.moving_right = self.moving_left = self.moving_up = self.moving_down = False
        self.moving_speed = 1.

    def move(self):
        if self.moving_right and self.rect.right + self.moving_speed <= self.screen_rect.right:
            self.rect.x += self.moving_speed
        elif self.moving_left and self.rect.left - self.moving_speed >= self.screen_rect.left:
            self.rect.x -= self.moving_speed
        elif self.moving_up and self.rect.top - self.moving_speed >= self.screen_rect.top:
            self.rect.y -= self.moving_speed
        elif self.moving_down and self.rect.bottom +self.moving_speed <= self.screen_rect.bottom:
            self.rect.y += self.moving_speed

    def blitme(self):
        self.screen.blit(self.img, self.rect)