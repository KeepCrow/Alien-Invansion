import pygame.font
from pygame.surface import Surface
from settings import Settings
from game_stats import GameStats


class ScoreBoard:
    """ 展示得分的类 """

    def __init__(self, game):
        self.screen: Surface = game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats: GameStats = game.stats

        # 显示得分时用的字体
        self.text_color = Settings.SCORE_BOARD_TEXT_COLOR
        self.text_size = Settings.SCORE_BOARD_TEXT_SIZE
        self.font = pygame.font.SysFont(None, self.text_size)

        # 渲染得分板图像
        self.render()

    def render(self):
        score_str = str(self.stats.score)
        self.score_img = self.font.render(score_str, True, self.text_color, Settings.BACKGROUND_COLOR)

        # 将图片放在右上角
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def blitme(self):
        """ 在屏幕上显示得分 """
        self.screen.blit(self.score_img, self.score_rect)