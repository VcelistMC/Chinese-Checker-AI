from audioop import minmax
from game_model import Game


class GameManager:
    def __init__(self, model: Game, view, diff=1) -> None:
        self.model = model
        self.view = view
        self.AI = "R"
        self.Human = "B"
        self.currentPlayer = self.Human
        self.currentlyHeldCell = None
        self.difficulty = diff
        self.holdingCell = False

    def move(self, cell):
        # we have to do extra shit here to validate the move and assert that the player
        # is holding the valid balls and stuff and switch turns
        # tommorrow tommorow 

        if not self.holdingCell:
            self.currentlyHeldCell = cell
            self.holdingCell = True
        else:
            self.model.move(self.currentlyHeldCell[0], self.currentlyHeldCell[1], cell[0], cell[1])
            self.view.update()
            self.holdingCell = False

    def max_score(self, state1, state2):
        return state1 if state1[1] > state2[1] else state2

    def min_score(self, state1, state2):
        return state1 if state1[1] < state2[1] else state2



    def minimax(self, model, player, depth, move):
        self.model.printBoard()
        if model.is_win(player) or depth == 0:
            return [move, self.evalBoard(player)]

        playerBalls = self.model.getPlayerBalls(player)

        for playerBall in playerBalls:
            validMoves_for_balls = self.model.getAllValidMoves(playerBall[0], playerBall[1])

            for validMove in validMoves_for_balls:
                if player == self.Human:
                    score = [None, -9000]

                    model.move(playerBall[0], playerBall[1], validMove[0], validMove[1])
                    score = self.max_score(score, self.minimax(model, self.AI, depth - 1, move))
                    model.move(validMove[0], validMove[1], playerBall[0], playerBall[1])
                    return score

                else:
                    score = [None, 9000]

                    model.move(playerBall[0], playerBall[1], validMove[0], validMove[1])
                    score = self.min_score(score, self.minimax(model, self.Human, depth - 1, validMove))
                    model.move(validMove[0], validMove[1], playerBall[0], playerBall[1])

                    return score


    def getNextBestMove(self):
        AI_Balls = self.model.getPlayerBalls(self.AI)
        states = []
        for ball in AI_Balls:
            state = self.minimax(self.model, ball, self.AI, self.difficulty)
            states.append(state)

        best_state = states[0]
        for state in states:
            best_state = self.max_score(best_state, state)

        return best_state

    def evalBoard(self, player):
        balls = self.model.getPlayerBalls(player)
        self.model.printBoard()
        goal = []
        distance = 0
        if player == self.Human:
            goal = [0, 12]
        else:
            goal = [16, 12]

        for ball in balls:
            distance += abs(ball[0] - goal[0]) + abs(ball[1] - goal[1])

        return distance


game = Game()
gamemanage = GameManager(game, None, 1)
# game.printBoard()
move = gamemanage.minimax(game, gamemanage.AI, 2, [3, 13])[0]
# print(/move)
# game.printBoard()
# gamemanage.model.move(3, 13, move[0], move[1])
# move = gamemanage.minimax(game, gamemanage.AI, 2, move)
# game.printBoard()
lis =[]