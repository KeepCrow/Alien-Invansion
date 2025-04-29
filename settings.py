import math


class Settings:
    # 主界面设置
    BACKGROUND_COLOR = (230, 230, 230)
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 1294
    GAME_TITLE = 'Alien Invasion'

    # 飞船设置
    SHIP_IMG = 'imgs/ship.png'
    SHIP_LIMIT = 3

    # 子弹设置
    BULLET_WIDTH = 3
    BULLET_HEIGHT = 15
    BULLET_COLOR = (60, 60, 60)

    # 外星人设置
    ALIEN_IMG = 'imgs/alien.png'
    ALIEN_WIDTH = 61
    ALIEN_HEIGHT = 67

    AVALIABLE_SPACE_X = SCREEN_WIDTH - (2 * ALIEN_WIDTH)
    NUMBER_ALIEN_X = math.ceil(AVALIABLE_SPACE_X / (2 * ALIEN_WIDTH))
    AVALIABLE_SPACE_Y = SCREEN_HEIGHT // 2 - (2 * ALIEN_HEIGHT)
    NUMBER_ALIEN_Y = AVALIABLE_SPACE_Y // (2 * ALIEN_HEIGHT)

    # 按钮设置
    BUTTON_WIDTH = 200
    BUTTON_HEIGTH = 50
    BUTTON_COLOR = (0, 135, 0)
    BUTTON_TEXT_COLOR = (255, 255, 255)
    BUTTON_TEXT_SIZE = 48

    # 得分板设置
    SCORE_BOARD_TEXT_COLOR = (30, 30, 30)
    SCORE_BOARD_TEXT_SIZE = 48
    ALIEN_SCORE = 40

    # 难度攀升设置
    SPEEDUP_SCALE = 1.1
    SCOREUP_SCALE = 1.5

    @classmethod
    def level_up(cls):
        cls.SHIP_SPEED *= cls.SPEEDUP_SCALE
        cls.BULLET_SPEED *= cls.SPEEDUP_SCALE
        cls.ALIEN_SPEED *= cls.SPEEDUP_SCALE
        cls.ALIEN_SCORE *= cls.SCOREUP_SCALE

    @classmethod
    def reset(cls):
        cls.SHIP_SPEED = 1.
        cls.ALIEN_SPEED = .1
        cls.ALIEN_FLEET_DROP_SPEED = cls.ALIEN_HEIGHT
        # 1 表示右移，-1表示左移
        cls.ALIEN_FLEET_DIRECTION = 1
        cls.BULLET_SPEED = 1.
