## Three Cups and a Ball Game

An interactive Python game inspired by the classic shell game. The player tracks a hidden ball as three cups are shuffled with increasing speed and complexity.

### Overview

This project simulates a fast-paced visual memory game where a ball is hidden under one of three cups. The cups are shuffled multiple times, and the player must correctly identify the ball’s location.

The game progressively increases in difficulty by speeding up animations and increasing the number of swaps after each correct guess.

### Features

- Animated cup movement using smooth arc-based transitions
- Increasing difficulty based on player performance
- Real-time user input and feedback
- High score tracking across rounds
- Modular game structure with separated logic and rendering

### How It Works

- The ball is randomly placed under one of three cups
- Cups are shuffled visually using animated swaps
- The player selects a cup after the shuffle
- If correct:
  - Score increases
  - Game becomes faster and more complex
- If incorrect:
  - Game resets and displays final score

### Technical Details

- Built using Python and `Draw.py` for graphics
- Event-driven game loop for continuous interaction
- Uses lists to maintain synchronization between visual positions and game state
- Trigonometric functions used to create smooth arc animations for cup swaps
- Difficulty scaling controlled by adjustable constants

### Setup
This project uses Draw.py for graphics.

### How to Run

Make sure `Draw.py` is installed and available.

Run the game:

```bash
python SemesterProject.py
