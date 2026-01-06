import random

def validate_move(move, bomb_used):
    valid_moves = ["rock", "paper", "scissors", "bomb"]
    if move not in valid_moves:
        return False, "Invalid move."
    if move == "bomb" and bomb_used:
        return False, "Bomb already used."
    return True, "Valid move."

def resolve_round(user_move, bot_move):
    if user_move == bot_move:
        return "draw"
    if user_move == "bomb":
        return "user"
    if bot_move == "bomb":
        return "bot"

    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if rules[user_move] == bot_move:
        return "user"
    return "bot"
