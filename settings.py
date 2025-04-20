import math


class Settings:
    # 主界面设置
    BACKGROUND_COLOR = (230, 230, 230)
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 1294
    GAME_TITLE = 'Stars Invasion'

    # 外星人设置
    STAR_IMG = 'imgs/star.png'
    STAR_WIDTH = 17
    STAR_HEIGHT = 23

    AVALIABLE_SPACE_X = SCREEN_WIDTH - (2 * STAR_WIDTH)
    NUMBER_STAR_X = math.ceil(AVALIABLE_SPACE_X / (2 * STAR_WIDTH))
    AVALIABLE_SPACE_Y = SCREEN_HEIGHT // 2 - (2 * STAR_HEIGHT)
    NUMBER_STAR_Y = AVALIABLE_SPACE_Y // (2 * STAR_HEIGHT)
