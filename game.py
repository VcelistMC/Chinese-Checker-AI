class Game:
	def initBoard(self):
		self.newBoard = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
		self.newBoard[0][12] = "G"
		self.newBoard[1][11] = "G"
		self.newBoard[1][13] = "G"
		self.newBoard[2][10] = "G"
		self.newBoard[2][12] = "G"
		self.newBoard[2][14] = "G"
		self.newBoard[3][9] = "G"
		self.newBoard[3][11] = "G"
		self.newBoard[3][13] = "G"
		self.newBoard[3][15] = "G"

		self.newBoard[4][0] = "B"
		self.newBoard[4][2] = "B"
		self.newBoard[4][4] = "B"
		self.newBoard[4][6] = "B"
		self.newBoard[5][1] = "B"
		self.newBoard[5][3] = "B"
		self.newBoard[5][5] = "B"
		self.newBoard[6][2] = "B"
		self.newBoard[6][4] = "B"
		self.newBoard[7][3] = "B"

		self.newBoard[9][3] = "P"
		self.newBoard[10][2] = "P"
		self.newBoard[10][4] = "P"
		self.newBoard[11][1] = "P"
		self.newBoard[11][3] = "P"
		self.newBoard[11][5] = "P"
		self.newBoard[12][0] = "P"
		self.newBoard[12][2] = "P"
		self.newBoard[12][4] = "P"
		self.newBoard[12][6] = "P"

		self.newBoard[9][21] = "O"
		self.newBoard[10][20] = "O"
		self.newBoard[10][22] = "O"
		self.newBoard[11][19] = "O"
		self.newBoard[11][21] = "O"
		self.newBoard[11][23] = "O"
		self.newBoard[12][18] = "O"
		self.newBoard[12][20] = "O"
		self.newBoard[12][22] = "O"
		self.newBoard[12][24] = "O"

		self.newBoard[4][18] = "Y"
		self.newBoard[4][20] = "Y"
		self.newBoard[4][22] = "Y"
		self.newBoard[4][24] = "Y"
		self.newBoard[5][19] = "Y"
		self.newBoard[5][21] = "Y"
		self.newBoard[5][23] = "Y"
		self.newBoard[6][20] = "Y"
		self.newBoard[6][22] = "Y"
		self.newBoard[7][21] = "Y"

		self.newBoard[16][12] = "R"
		self.newBoard[15][11] = "R"
		self.newBoard[15][13] = "R"
		self.newBoard[14][10] = "R"
		self.newBoard[14][12] = "R"
		self.newBoard[14][14] = "R"
		self.newBoard[13][9] = "R"
		self.newBoard[13][11] = "R"
		self.newBoard[13][13] = "R"
		self.newBoard[13][15] = "R"

		self.newBoard[4][8] = "."	
		self.newBoard[4][10] = "."	
		self.newBoard[4][12] = "."	
		self.newBoard[4][14] = "."	
		self.newBoard[4][16] = "."			
		
		self.newBoard[5][7] = "."	
		self.newBoard[5][9] = "."	
		self.newBoard[5][11] = "."	
		self.newBoard[5][13] = "."	
		self.newBoard[5][15] = "."	
		self.newBoard[5][17] = "."
		
		self.newBoard[6][6] = "."	
		self.newBoard[6][8] = "."	
		self.newBoard[6][10] = "."	
		self.newBoard[6][12] = "."	
		self.newBoard[6][14] = "."	
		self.newBoard[6][16] = "."	
		self.newBoard[6][18] = "."
		
		self.newBoard[7][5] = "."	
		self.newBoard[7][7] = "."	
		self.newBoard[7][9] = "."	
		self.newBoard[7][11] = "."	
		self.newBoard[7][13] = "."	
		self.newBoard[7][15] = "."	
		self.newBoard[7][17] = "."	
		self.newBoard[7][19] = "."

		self.newBoard[8][4] = "."	
		self.newBoard[8][6] = "."	
		self.newBoard[8][8] = "."	
		self.newBoard[8][10] = "."	
		self.newBoard[8][12] = "."	
		self.newBoard[8][14] = "."	
		self.newBoard[8][16] = "."	
		self.newBoard[8][18] = "."	
		self.newBoard[8][20] = "."
		
		self.newBoard[9][5] = "."	
		self.newBoard[9][7] = "."	
		self.newBoard[9][9] = "."	
		self.newBoard[9][11] = "."	
		self.newBoard[9][13] = "."	
		self.newBoard[9][15] = "."	
		self.newBoard[9][17] = "."	
		self.newBoard[9][19] = "."

		self.newBoard[10][6] = "."	
		self.newBoard[10][8] = "."	
		self.newBoard[10][10] = "."	
		self.newBoard[10][12] = "."	
		self.newBoard[10][14] = "."	
		self.newBoard[10][16] = "."	
		self.newBoard[10][18] = "."

		self.newBoard[11][7] = "."	
		self.newBoard[11][9] = "."	
		self.newBoard[11][11] = "."	
		self.newBoard[11][13] = "."	
		self.newBoard[11][15] = "."	
		self.newBoard[11][17] = "."

		self.newBoard[12][8] = "."	
		self.newBoard[12][10] = "."	
		self.newBoard[12][12] = "."	
		self.newBoard[12][14] = "."	
		self.newBoard[12][16] = "."
	
	def __init__(self):
		self.cols = 25
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
				print(self.newBoard[i][j], end=" ")
			print("\n")

	# executes a move, Note: This function assumes that the given next move is valid
	def move(self, pieceRow, pieceCol, destRow, destCol):
		self.newBoard[destRow][destCol] = self.newBoard[pieceRow][pieceCol]
		self.newBoard[pieceRow][pieceCol] = "."

	# get all moves from starting pos
	def getMoves(self, pieceRow, pieceCol):
		moves = {}

		for dir, cords in self.dirs.items():
			newRow = pieceRow + cords[0]
			newCol = pieceCol + cords[1]
			if newRow < 0 or newCol < 0 or newRow >= self.rows or newCol >= self.cols or self.newBoard[newRow][newCol] == " ":
				continue
			moves[dir] = [newRow, newCol]
		return moves
	

	def getAllValidMoves(self,  pieceRow, pieceCol) -> list:
		allMoves = self.getMoves(pieceRow, pieceCol)
		validMoves = []
		for dir, move in allMoves.items():
			row = move[0]
			col = move[1]
			if self.newBoard[row][col] == ".":
				validMoves.append(move)
				continue
			
			dirMove = self.dirs[dir]
			newRow = row + dirMove[0]
			newCol = col + dirMove[1]

			if self.newBoard[newRow][newCol] == ".":
				validMoves.append([newRow, newCol])

		return validMoves

		
		

			

game = Game()

# print(moves)
print(game.getAllValidMoves(2, 12))
# game.printBoard()



