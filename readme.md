# Chinese Checkers AI Agent

An AI agent capable of playing Chinese Checkers using Minmax Algorithm with varying levels of difficulty.

## How the AI decides
The board is represented as a 17x25 array of strings, with `“R”` representing the AI, `“B”` representing the player and `“.”` representing  an empty cell. Each player’s goal is to move all of their set of marbles to the opposite side of the board (replacing the opponent’s marbles)
Each player has the furthest opposite cell vertex as their goal, so the board is scored based on the sum of each marble’s distance and the goal vertex using Euclidean distance
```py
# game_controller.py
def euclidean_distance(self, start, end):    
    num1 = pow(end[0] - start[0], 2)    
    num2 = pow(end[1] - start[1], 2) // 2    
    return sqrt(num1 + num2)
```
The AI decides based on the difference between its board score and the human board score, so naturally, a negative score indicates that the player is closer to the goal than the AI and vice versa
## How to run this gmae
1. First install the project requirements
```
pip install requirements.txt
```
2. simply run the `main.py` file with the difficulty of choice (1 for easy, 3 for medium and 5 for hard)
```
python main.py [difficulty]
```

## ScreenShots
![Game Start](Screenshots/gameStart.png)
![mid game](Screenshots/midGame.png)
![Ai winning](Screenshots/aiWin.png)
