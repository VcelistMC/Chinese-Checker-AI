from math import sqrt
from game_model import Game


class GameManager:
    def __init__(self, model: Game, view, diff=1) -> None:
        self.model = model
        self.view = view
        self.AI = "R"
        self.Human = "B"
        self.MAX_SCORE = 9000
        self.currentlyHeldCell = None
        self.difficulty = diff
        self.holdingCell = False

    def move(self, cell):
        ball = self.model.getBall(cell[0], cell[1])
        if (ball == "." and not self.holdingCell) or ball == self.AI: return
        
        if ball == self.Human and self.holdingCell:
            self.currentlyHeldCell = cell
            self.view.update()
            self.view.setValidMoves(self.model.getAllValidMoves(cell[0], cell[1]))
            return

        if not self.holdingCell:
            self.currentlyHeldCell = cell
            self.holdingCell = True
            self.view.update()
            self.view.setValidMoves(self.model.getAllValidMoves(cell[0], cell[1]))
            return 
        else:
            if tuple(cell) not in self.model.getAllValidMoves(self.currentlyHeldCell[0], self.currentlyHeldCell[1]):
                return
            self.model.move(self.currentlyHeldCell[0], self.currentlyHeldCell[1], cell[0], cell[1])
            self.view.changeTurn("AI")
            self.view.update()
            self.holdingCell = False

            
            if self.model.is_win(self.Human):
                self.view.declareWinner("Player")
                return        
        
        self.currentlyHeldCell, nextMove = self.getNextBestMove()
        self.model.move(self.currentlyHeldCell[0], self.currentlyHeldCell[1], nextMove[0], nextMove[1])
        self.view.update()
        if self.model.is_win(self.AI): 
            self.view.declareWinner("AI")
        self.view.changeTurn("Human")


    def minimax(self, model, player, depth, alpha, beta):
        
        playerWon = model.is_win(player)
        if playerWon:
            if player == self.AI:
                print("AI won")
                return self.MAX_SCORE
            else: 
                print("Human won")
                return -self.MAX_SCORE

        elif depth == 0:
            return self.evalBoard(model, self.Human) - self.evalBoard(model, self.AI)


        if player == self.AI:
            score = -self.MAX_SCORE

            ai_pieces = model.getPlayerBalls(self.AI)
            for piece in ai_pieces:
                validMoves = model.getAllValidMoves(piece[0], piece[1])

                for validMove in validMoves:
                    model.move(piece[0], piece[1], validMove[0], validMove[1]) 
                    score = max(score, self.minimax(model, self.Human, depth - 1, alpha, beta))
                    model.move(validMove[0], validMove[1], piece[0], piece[1])

                    alpha = max(alpha, score)
                    if beta <= alpha:
                        return score
                    
            return score
        else:
            score = self.MAX_SCORE
            human_pcs = model.getPlayerBalls(self.Human)
            for piece in human_pcs:
                validMoves = model.getAllValidMoves(piece[0], piece[1])
                
                for validMove in validMoves:
                    model.move(piece[0], piece[1], validMove[0], validMove[1])
                    score = min(score, self.minimax(model, self.AI, depth - 1, alpha, beta))
                    model.move(validMove[0], validMove[1], piece[0], piece[1])

                    beta = min(beta, score)
                    if beta <= alpha:
                        return score
            return score



    def getNextBestMove(self):
        nextMove = None
        piece_to_move = None
        bestScore = -self.MAX_SCORE

        aiPieces = self.model.getPlayerBalls(self.AI)

        for piece in aiPieces:
            validMoves = self.model.getAllValidMoves(piece[0], piece[1])
            for validMove in validMoves:
                
                self.model.move(piece[0], piece[1], validMove[0], validMove[1])
                score = self.minimax(self.model, self.Human, self.difficulty, -self.MAX_SCORE, self.MAX_SCORE)
                self.model.move(validMove[0], validMove[1], piece[0], piece[1])


                if score > bestScore:
                    nextMove = validMove
                    bestScore = score
                    piece_to_move = piece
        

        return piece_to_move, nextMove

    def euclidean_distance(self, start, end):
        num1 = pow(end[0] - start[0], 2)
        num2 = pow(end[1] - start[1], 2) // 2
        return int(sqrt(num1 + num2))

    def manhattan_distance(self, start, end):
        row_diff = abs(end[0] - start[0])
        col_diff = abs(end[1] - start[1])

        return row_diff + col_diff


    def evalBoard(self, model, player):
        goal = [0,12] if player == self.Human else [16,12]
        
        distance = 0
        balls = model.getPlayerBalls(player)
        for ball in balls:
            distance +=  self.euclidean_distance(ball, goal)

        return distance

