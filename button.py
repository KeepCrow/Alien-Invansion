import pygame
from pygame.surface import Surface
from settings import Settings


class Button:
    """ 为游戏创建一个按钮类 """

    def __init__(self, game, msg: str):
        """ 初始化按钮属性 """
        self.screen: Surface = game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮属性
        self.width, self.heigth = Settings.BUTTON_WIDTH, Settings.BUTTON_HEIGTH
        self.color = Settings.BUTTON_COLOR
        self.text_color = Settings.BUTTON_TEXT_COLOR
        self.text_size = Settings.BUTTON_TEXT_SIZE

        # 创建按钮对象，使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.heigth)
        self.rect.center = self.screen_rect.center

        # 按钮标签仅创建一次
        self._render(msg)

    def _render(self, msg: str):
        """ 将msg渲染为图像，并使其在按钮上居中 """
        font = pygame.font.SysFont('幼圆', self.text_size)
        self.msg_image = font.render(msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def blitme(self):
        """ 绘制一个用颜色填充的按钮，再绘制文本 """
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

