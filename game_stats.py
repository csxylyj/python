import json


class GameStats:
    """游戏信息统计"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self.read_high_score()

    def reset_stats(self):
        """游戏信息统计"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        """"读取最高分"""
        with open('high_score.txt', 'r') as file_object:
            number = json.load(file_object)
        return number

    def write_high_score(self, score):
        filename = 'high_score.txt'
        with open(filename, 'a') as f:
            f.seek(0)
            f.truncate()
            f.write(str(score))
