import pygame
from pygame.sprite import Sprite
 
class Bullet(Sprite):
    """飞船发射子弹"""

    def __init__(self, ai_game):
        """创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 创建一个矩形表示子弹并设置位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储用小数表示子弹的位置
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.settings.bullet_speed
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

        """向右移动子弹"""
        # 更新表示子弹位置的小数值
        # self.x -= self.settings.bullet_speed
        # 更新表示子弹的rect的位置
        # self.rect.x =self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)