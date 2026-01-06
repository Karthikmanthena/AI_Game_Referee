class GameState:
    def __init__(self):
        self.round = 1
        self.max_rounds = 3
        self.user_score = 0
        self.bot_score = 0
        self.user_bomb_used = False
        self.bot_bomb_used = False

    def is_game_over(self):
        return self.round > self.max_rounds
