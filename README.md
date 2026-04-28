# 3-Cups-and-a-Ball-Game
An interactive Python game that simulates the classic three-cup shell game, where a ball is hidden under one cup and shuffled. The project uses an event-driven structure with modular functions for game logic, rendering, animation, and user input.

Cup movements are animated using trigonometric functions to create smooth arc-based swaps instead of simple linear motion. The game includes dynamic difficulty scaling, increasing both the speed and number of swaps as the player continues to guess correctly, along with high score tracking for replayability.

Data structures are used to keep the visual state and underlying logic synchronized throughout each round, all managed through a central game loop that controls progression and scoring.
