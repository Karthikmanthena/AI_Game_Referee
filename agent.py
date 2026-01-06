import random
from tools import validate_move, resolve_round

class GameAgent:
    def __init__(self, state):
        self.state = state

    def get_bot_move(self):
        choices = ["rock", "paper", "scissors"]
        if not self.state.bot_bomb_used:
            choices.append("bomb")
        return random.choice(choices)

    def play_round(self, user_move):
        valid, msg = validate_move(user_move, self.state.user_bomb_used)

        bot_move = self.get_bot_move()

        if not valid:
            result = "bot"
        else:
            if user_move == "bomb":
                self.state.user_bomb_used = True
            if bot_move == "bomb":
                self.state.bot_bomb_used = True

            result = resolve_round(user_move, bot_move)

        if result == "user":
            self.state.user_score += 1
        elif result == "bot":
            self.state.bot_score += 1

        output = {
            "round": self.state.round,
            "user_move": user_move,
            "bot_move": bot_move,
            "result": result
        }

        self.state.round += 1
        return output
