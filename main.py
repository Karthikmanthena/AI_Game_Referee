from game_state import GameState
from agent import GameAgent

def run_game():
    print("Welcome to Rock–Paper–Scissors–Plus!")

    user_name = input("Enter your name: ").strip()
    if not user_name:
        user_name = "Player"

    while True:
        state = GameState()
        agent = GameAgent(state)

        print(f"\nHello {user_name}! 👋")
        print("Rules: Best of 3 rounds.")
        print("Moves: rock, paper, scissors, bomb")
        print("Bomb can be used once. Bomb beats all. Invalid input wastes the round.\n")

        while not state.is_game_over():
            move = input(f"Round {state.round} — {user_name}, enter your move: ").lower()
            result = agent.play_round(move)

            print(f"{user_name}: {result['user_move']} | Bot: {result['bot_move']}")

            if result['result'] == "draw":
                print("Round result: Draw")
            else:
                winner = user_name if result['result'] == "user" else "Bot"
                print(f"Round winner: {winner}")

            print(f"Score → {user_name}: {state.user_score} | Bot: {state.bot_score}\n")

        print("Game Over!")
        if state.user_score > state.bot_score:
            print(f"🏆 Final Result: {user_name} Wins!")
        elif state.bot_score > state.user_score:
            print("🏆 Final Result: Bot Wins!")
        else:
            print("🤝 Final Result: Draw!")

        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice != "yes":
            print(f"\nThanks for playing, {user_name}! 👋")
            break

def main():
    run_game()

if __name__ == "__main__":
    main()
