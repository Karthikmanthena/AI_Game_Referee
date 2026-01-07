# 🎮 AI Game Referee — Rock–Paper–Scissors–Plus

## 📌 Overview
This project implements a minimal AI referee chatbot that conducts a short game of Rock–Paper–Scissors–Plus between a user and the bot. The system enforces game rules, tracks state across turns, validates player inputs, and provides clear round-by-round feedback, fulfilling all functional and technical requirements of the assignment.

The application runs as a conversational CLI program and demonstrates clean separation between intent handling, game logic, and response generation.

---

## 🧠 Game Rules
- The game is **best of 3 rounds**
- Valid moves: `rock`, `paper`, `scissors`, `bomb`
- Each player may use `bomb` **only once per game**
- `bomb` defeats all other moves
- `bomb` vs `bomb` results in a **draw**
- Invalid input **wastes the round**
- After 3 rounds, the game **automatically ends**

---

## 🏗️ Architecture & Design

### State Model (`game_state.py`)
The `GameState` class stores and persists all critical information:
- Current round number
- Maximum rounds
- Player scores
- Bomb usage flags for both players

This ensures that the game state is never stored only in the prompt and remains consistent across turns.

### Game Tools (`tools.py`)
Explicit game tools are implemented to enforce logic:
- `validate_move()` — validates user input and enforces bomb constraints
- `resolve_round()` — determines the winner of each round based on rules

These tools handle state validation and mutation as required by the assignment.

### Agent Layer (`agent.py`)
The `GameAgent` class:
- Interprets player intent
- Chooses bot moves
- Applies game logic through tools
- Updates game state
- Produces structured round outcomes

### Interface Layer (`main.py`)
Handles:
- User interaction
- Rule explanation
- Turn prompting
- Output generation
- Final result reporting
- Play-again loop

This separation maintains clarity between logic, state, and responses.

---

## 🧪 Functional Features
- Clear rule explanation (≤5 lines)
- Robust input validation
- Graceful handling of invalid input
- Automatic game termination after 3 rounds
- Round-by-round feedback:
  - Round number
  - Player & bot moves
  - Round winner
- Final match result
- User name support
- Continuous play option

---

## ⚙️ Installation & Execution

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
