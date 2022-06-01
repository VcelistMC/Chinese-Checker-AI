class Game:
    def initBoard(self):
        self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
        
        #init top start
        start_ind = 12
        end_ind = 12

        for row in range(0, 4):
            for col in range(start_ind, end_ind+1, 2):
                self.board[row][col] = self.players[0]
            start_ind -= 1
            end_ind += 1

        #init first section with dots
        start_ind = 0
        end_ind = 24

        for row in range(4, 9):
            for col in range(start_ind, end_ind+1, 2):
                self.board[row][col] = "."

            start_ind += 1
            end_ind -= 1
        
        #init second empty section with dots
        start_ind = 3
        end_ind = 21

        for row in range(9, 13):
            for col in range(start_ind, end_ind+1, 2):
                self.board[row][col] = "."
            start_ind -= 1
            end_ind += 1
        
        #init bottom star
        start_ind = 9
        end_ind = 15
        for row in range(13, 17):
            for col in range(start_ind, end_ind+1, 2):
                self.board[row][col] = self.players[1]
            start_ind += 1
            end_ind -= 1

    def __init__(self):
        self.cols = 25
        self.players = ["R", "B"]
        self.rows = 17
        self.rowsLengths = [1, 2, 3, 4, 13, 12, 11, 10, 9, 10, 11, 12, 13, 4, 3, 2, 1]

        self.dirs = {}
        self.dirs.setdefault("north west", [-1, -1])
        self.dirs.setdefault("north east", [-1, 1])
        self.dirs.setdefault("east", [0, 2])
        self.dirs.setdefault("west", [0, -2])
        self.dirs.setdefault("south west", [1, -1])
        self.dirs.setdefault("south east", [1, 1])

        self.initBoard()

    def printBoard(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.board[i][j], end=" ")
            print("\n")

    # executes a move, Note: This function assumes that the given next move is valid
    def move(self, pieceRow, pieceCol, destRow, destCol):
        self.board[destRow][destCol] = self.board[pieceRow][pieceCol]
        self.board[pieceRow][pieceCol] = "."

    # get all moves from starting pos
    def getMoves(self, pieceRow, pieceCol):
        moves = {}

        for dir, cords in self.dirs.items():
            newRow = pieceRow + cords[0]
            newCol = pieceCol + cords[1]
            if newRow < 0 or newCol < 0 or newRow >= self.rows or newCol >= self.cols or self.board[newRow][
                newCol] == " ":
                continue
            moves[dir] = [newRow, newCol]
        return moves

    def getAllValidMoves(self, pieceRow, pieceCol) -> list:
        allMoves = self.getMoves(pieceRow, pieceCol)
        validMoves = []
        for dir, move in allMoves.items():
            row = move[0]
            col = move[1]
            if self.board[row][col] == ".":
                validMoves.append(move)
                continue

            dirMove = self.dirs[dir]
            newRow = row + dirMove[0]
            newCol = col + dirMove[1]

            if self.board[newRow][newCol] == ".":
                validMoves.append([newRow, newCol])

        return validMoves


    def is_win(self, player):
        player1Count = 0
        if player == "R":
            start_index = 12
            end_index = 12
            for row in range(4):
                for col in range(start_index, end_index+1, 2):
                    if self.board[row][col] == "R":
                        player1Count += 1
                start_index -= 1
                end_index += 1

        else:
            start_index = 12
            end_index = 12
            for row in range(13, 17):
                for col in range(start_index, end_index + 1, 2):
                    if self.board[row][col] == "G":
                        player1Count += 1

                start_index -= 1
                end_index += 1

        return player1Count == 10



game = Game()

# # print(moves)
game.printBoard()
# # print(game.getAllValidMoves(2, 12))
# # game.printBoard()
# print(game.is_win("R"))
