import sys
import time
import pygame
from pygame.event import Event
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


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
        # 新建一个外星人组
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # 新建一个信息统计实例
        self.stats = GameStats(self)
        # 新建游戏启动后的状态
        self.game_active = True

        # 设置窗口标题
        pygame.display.set_caption(Settings.GAME_TITLE)

    def _create_fleet(self):
        """ 创建外星人群 """
        for row in range(Settings.NUMBER_ALIEN_Y):
            for col in range(Settings.NUMBER_ALIEN_X):
                self.aliens.add(self._create_alien(row, col))

    def _create_alien(self, row: int, column: int) -> Alien:
        alien = Alien(self)
        alien.x = Settings.ALIEN_WIDTH + 2 * Settings.ALIEN_WIDTH * column
        alien.rect.x = alien.x
        alien.y = Settings.ALIEN_HEIGHT + 2 * Settings.ALIEN_HEIGHT * row
        alien.rect.y = alien.y
        return alien

    def run_game(self):
        """ 游戏主循环 """
        while True:
            # 处理事件
            self._check_events()

            if self.game_active:
                # 更新飞船位置
                self.ship.update()
                # 更新子弹的位置
                self._update_bullets()
                # 更新外星人的位置
                self._update_aliens()

            # 绘制屏幕
            self._update_screen()

    def _update_bullets(self):
        """ 更新子弹的位置，删除消失的子弹 """
        self.bullets.update()

        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # 如果子弹击中外星人，删除子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # 如果外星人被消灭，再创建一群
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """ 检查是否存在外星人碰到了边界，并根据结果更新外星人位置 """
        if self._check_fleet_edges():
            self._change_fleet_direction()
        self.aliens.update()

        # 检测外星人是否撞到了飞船
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 检测外星人是否撞到了地面
        self._check_aliens_ground()

    def _check_aliens_ground(self):
        """ 检测是否有外星人到达了屏幕地面 """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= Settings.SCREEN_HEIGHT:
                """ 属于失败的清空，与飞船被撞一样处理 """
                self._ship_hit()
                break

    def _ship_hit(self):
        """ 响应飞船与外星人的碰撞 """
        if self.stats.remain_ship <= 0:
            self.game_active = False
            return

        # 剩余飞船数量减一
        self.stats.remain_ship -= 1

        # 清空外星人和子弹
        self.bullets.empty()
        self.aliens.empty()

        # 新建一组外星人，重置飞船飞船
        self._create_fleet()
        self.ship.center_ship()

        # 暂停半秒
        time.sleep(0.5)

    def _check_fleet_edges(self):
        """ 是否有任意一个外星人碰到了边界 """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                return True
        return False

    def _change_fleet_direction(self):
        """ 将整群外星人下移，并改变方向 """
        for alien in self.aliens.sprites():
            alien.drop()
        Settings.ALIEN_FLEET_DIRECTION *= -1

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
        # 重绘所有外星人
        for alien in self.aliens.sprites():
            alien.blitme()
        # 使最近的绘制可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
