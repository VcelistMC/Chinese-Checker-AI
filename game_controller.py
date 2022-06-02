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
        return state1 if state1[1] > state2[2] else state2

    def min_score(self, state1, state2):
        return state1 if state1[1] < state2[2] else state2

    def minimax(self, model, move, player, depth):
        if model.is_win(player) or depth == 0:
            return [move, self.evalBoard(player)]

        if player == self.Human:
            score = [None, -9000]
            validMoves = model.getAllValidMoves(move)
            for validMove in validMoves:
                model.move(move[0], move[1], validMove[0], validMove[1])
                score = self.max_score(score, self.minimax(model, validMove, self.AI, depth - 1))
                model.move(validMove[0], validMove[1], move[0], move[1])
            return score

        else:
            score = [None, 9000]
            validMoves = model.getAllValidMoves(move)
            for validMove in validMoves:
                model.move(move[0], move[1], validMove[0], validMove[1])
                score = self.min_score(score, self.minimax(model, validMove, self.Human, depth - 1))
                model.move(validMove[0], validMove[1], move[0], move[1])

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
game.printBoard()
gamemanage = GameManager(game, None, 1)
game.move(3,13,4,12)
print(gamemanage.evalBoard(player=gamemanage.AI))
