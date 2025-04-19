import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """ 管理游戏资源和行为的类 """

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()

        # 新建一个分辨率为1200*1942的主界面
        self.screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
        self.ship = Ship(self)

        # 设置窗口标题
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """ 游戏主循环 """
        while True:
            # 监视键盘及鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # 将整个界面绘制为背景色
            self.screen.fill(Settings.bgcolor)
            self.ship.blitme()

            # 使最近的绘制可见
            pygame.display.flip()
        

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
