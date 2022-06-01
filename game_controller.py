from game_model import Game


class GameManager:
    def __init__(self, model, view, diff = 1) -> None:
            self.model = model
            self.view = view
            self.player1Color = "R"
            self.player2Color = "B"
            self.difficulty = diff

    def minimax(self, board, move, maxPlayer, depth):
        if board.is_win() or depth == 0:
            return [move, self.evalBoard(board)]

        if maxPlayer:
            validMoves = board.getAllValidMoves(move)
            for validMove in validMoves:
                score = max(score, self.minimax(board, validMove, False, depth-1))

        else:
            validMoves = board.getAllValidMoves(move)
            for validMove in validMoves:
                score = min(score, self.minimax(board, validMove, True, depth-1)) 
    
    def getNextBestMove(self):
        my_balls = []
        scores = []
        for my_ball in my_balls:
            score = self.minimax(self.model, my_ball, True, self.difficulty)
            scores.append(score)
        
        score = -1
        nextBestMove = []
        for nextMove in scores:
            if score > nextMove[0]:
                