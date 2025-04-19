import math


class Settings:
    # 主界面设置
    BACKGROUND_COLOR = (230, 230, 230)
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 1294
    GAME_TITLE = 'Alien Invasion'

    # 飞船设置
    SHIP_IMG = 'imgs/ship.png'
    SHIP_SPEED = 1.

    # 子弹设置
    BULLET_SPEED = 1.
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
