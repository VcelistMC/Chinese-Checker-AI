from game_model import Game


class GameManager:
    def __init__(self, model: Game, view, diff=1) -> None:
        self.model = model
        self.view = view
        self.AI = "R"
        self.Human = "B"
        self.difficulty = diff

    def max_score(self, state1, state2):
        return state1 if state1[1] > state2[2] else state2

    def min_score(self, state1, state2):
        return state1 if state1[1] < state2[2] else state2

    def minimax(self, model, move, player, depth):
        if model.is_win(player) or depth == 0:
            return [move, self.evalBoard(model)]

        if player == self.Human:
            score = [None, -9000]
            validMoves = model.getAllValidMoves(move)
            for validMove in validMoves:
                score = self.max_score(score, self.minimax(model, validMove, self.AI, depth - 1))
            return score

        else:
            score = [None, 9000]
            validMoves = model.getAllValidMoves(move)
            for validMove in validMoves:
                score = self.min_score(score, self.minimax(model, validMove, self.Human, depth - 1))
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

    def evalBoard(self, board):
        pass
