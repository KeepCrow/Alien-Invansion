import sys
import pygame
from pygame.event import Event
from settings import Settings
from star import Star


class AlienInvasion:
    """ 管理游戏资源和行为的类 """

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()

        # 新建一个主界面
        self.screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        # 新建一个星星组
        self.stars = pygame.sprite.Group()
        self._create_fleet()

        # 设置窗口标题
        pygame.display.set_caption(Settings.GAME_TITLE)

    def _create_fleet(self):
        """ 创建星星群 """
        for row in range(Settings.NUMBER_STAR_Y):
            for col in range(Settings.NUMBER_STAR_X):
                self.stars.add(self._create_star(row, col))

    def _create_star(self, row: int, column: int) -> Star:
        star = Star(self)
        star.x = Settings.STAR_WIDTH + 2 * Settings.STAR_WIDTH * column
        star.rect.x = star.x
        star.y = Settings.STAR_HEIGHT + 2 * Settings.STAR_HEIGHT * row
        star.rect.y = star.y
        return star

    def run_game(self):
        """ 游戏主循环 """
        while True:
            # 处理事件
            self._check_events()
            # 更新星星的位置
            self.stars.update()
            # 绘制屏幕
            self._update_screen()

    def _check_events(self):
        """ 处理键盘和鼠标事件 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # 设置背景色
        self.screen.fill(Settings.BACKGROUND_COLOR)
        # 重绘所有星星
        for alien in self.stars.sprites():
            alien.blitme()
        # 使最近的绘制可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
