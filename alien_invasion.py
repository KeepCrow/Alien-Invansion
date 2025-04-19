import sys
import pygame
from pygame.event import Event
from ship import Ship


class AlienInvasion:
    def __init__(self):
        # 初始化Pygame
        pygame.init()

        # 创建窗口
        self.screen = pygame.display.set_mode((800, 900))
        self.bgcolor = (135, 206, 250)
        pygame.display.set_caption('外星人入侵')

        # 创建火箭
        self.ship = Ship(self)

    def run(self):
        while True:
            self.check_events()
            self.ship.move()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event: Event):
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def check_keyup_events(self, event: Event):
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    def update_screen(self):
        self.screen.fill(self.bgcolor)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    game = AlienInvasion()
    game.run()