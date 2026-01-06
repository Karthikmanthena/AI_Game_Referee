# AI_Game_Referee
AI Game Referee — Rock–Paper–Scissors–Plus

State Model:
The GameState object stores round number, scores, and bomb usage. State persists across turns and ends after three rounds.

Agent & Tool Design:
The GameAgent controls game flow. Validation and resolution are handled by explicit tools in tools.py. The agent interprets user intent, applies game logic, and generates responses.

Tradeoffs:
Kept design simple for clarity and reliability.

Future Improvements:
Better natural language understanding and UI interface.
