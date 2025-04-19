import sys
import pygame
from pygame.event import Event
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """ 管理游戏资源和行为的类 """

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()

        # 新建一个主界面
        self.screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        # 新建一个飞船
        self.ship = Ship(self)
        # 新建一个子弹组
        self.bullets = pygame.sprite.Group()

        # 设置窗口标题
        pygame.display.set_caption(Settings.GAME_TITLE)

    def run_game(self):
        """ 游戏主循环 """
        while True:
            # 处理事件
            self._check_events()
            # 更新飞船位置
            self.ship.update()
            # 更新子弹的位置
            self.bullets.update()
            # 删除飞出屏幕的子弹
            for bullet in self.bullets.sprites():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            # 绘制屏幕
            self._update_screen()

    def _fire(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_events(self):
        """ 处理键盘和鼠标事件 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event: Event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire()

    def _check_keyup_events(self, event: Event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # 设置背景色
        self.screen.fill(Settings.BACKGROUND_COLOR)
        # 重绘飞船
        self.ship.blitme()
        # 重绘所有子弹
        for bullet in self.bullets.sprites():
            bullet.drawme()
        # 使最近的绘制可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
