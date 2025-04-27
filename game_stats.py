from settings import Settings


class GameStats:
    """ 跟踪游戏的统计信息 """

    def __init__(self, game):
        self.reset_stats()

    def reset_stats(self):
        """ 初始化在游戏运行期间可能变换的统计信息 """
        self.remain_ship = Settings.SHIP_LIMIT
        self.curlevel = 1