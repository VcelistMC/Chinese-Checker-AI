from math import ceil, floor, sqrt
from os import system
from time import sleep


class Game:
	
	def initBoard(self):
		self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]

		# init top start
		start_ind = 12
		end_ind = 12

		for row in range(0, 4):
			for col in range(start_ind, end_ind + 1, 2):
				self.board[row][col] = "R"
			start_ind -= 1
			end_ind += 1

		# init first section with dots
		start_ind = 0
		end_ind = 24

		for row in range(4, 9):
			for col in range(start_ind, end_ind + 1, 2):
				self.board[row][col] = "."

			start_ind += 1
			end_ind -= 1

		# init second empty section with dots
		start_ind = 3
		end_ind = 21

		for row in range(9, 13):
			for col in range(start_ind, end_ind + 1, 2):
				self.board[row][col] = "."
			start_ind -= 1
			end_ind += 1

		# init bottom star
		start_ind = 9
		end_ind = 15
		for row in range(13, 17):
			for col in range(start_ind, end_ind + 1, 2):
				self.board[row][col] = "B"
			start_ind += 1
			end_ind -= 1




	def __init__(self):
		self.cols = 25
		self.rows = 17
		self.directions = {}
		self.directions.setdefault("north west", [-1, -1])
		self.directions.setdefault("north east", [-1, 1])
		self.directions.setdefault("east", [0, 2])
		self.directions.setdefault("west", [0, -2])
		self.directions.setdefault("south west", [1, -1])
		self.directions.setdefault("south east", [1, 1])
		self.AI = "R"
		self.Human = "B"

		self.initBoard()
		
	def eclidiean_distance(self, start, end):
		num1 = pow(end[0] - start[0], 2)
		num2 = pow(end[1] - start[1], 2) // 2
		return int(sqrt(num1 + num2)) 
		
	def inGoalReigon(self, player, cell):
		if player == self.AI:
			return  cell[0] >= 12
		else:
			return cell[0] < 4

	def printBoard(self):
		for i in range(self.rows):
			for j in range(self.cols):
					print(self.getBall(i, j), end = " ")
			print("\n")
	
	# executes a move, Note: This function assumes that the given next move is valid
	def move(self, pieceRow, pieceCol, destRow, destCol):
		self.board[destRow][destCol] = self.board[pieceRow][pieceCol]
		self.board[pieceRow][pieceCol] = "."

	# get all moves from starting pos
	def getMoves(self, pieceRow, pieceCol):
		moves = {}

		for dir, cords in self.directions.items():
			newRow = pieceRow + cords[0]
			newCol = pieceCol + cords[1]
			if self.isOutOfBounds(newRow, newCol):
				continue
			moves[dir] = [newRow, newCol]
		return moves
	
	def isOutOfBounds(self, row, col):
		return row < 0 or col < 0 or row >= self.rows or col >= self.cols or self.board[row][col] == " "

	# we can only do two types of moves
		# simple move -> moving to adjacent cell
		# hop -> hopping over a ball

	# if we hop, we have to hop again to keep moving, otherwise we stop
	
	def getAllValidMoves(self, pieceRow, pieceCol):
		moveSet = set()
		moveSet = self.getValidMoveRecu(pieceRow, pieceCol, moveSet, False)
		copySet = set(moveSet)
		ball = self.getBall(pieceRow, pieceCol)
		if ball == "B":
			if 0 <= pieceRow < 4:
				for move in moveSet:
					if move[0] > 3:
						copySet.remove(move)
		else:
			if 13 <= pieceRow < 17:
				for move in moveSet:
					if move[0] < 13:
						copySet.remove(move)
		return copySet

	def getValidMoveRecu(self, pieceRow, pieceCol, currValidMoves, isHopping):
		# get all possible moves (adjacent cells)
		allMoves = self.getMoves(pieceRow, pieceCol)
		for direction, move in allMoves.items():
			newRow = move[0]
			newCol = move[1]
			if (self.board[newRow][newCol] == "."):
				# did we hop last move, if we did, we can't do a simple move
				# we have to hop again to keep moving
				if not isHopping:
					currValidMoves.add((newRow, newCol))
				continue
			
			# apply the direction again to hop
			jumpdirection = self.directions[direction]
			jumpRow = newRow + jumpdirection[0]
			jumpCol = newCol + jumpdirection[1]
			
			
			if self.isOutOfBounds(jumpRow, jumpCol): continue

			# if the cell we jumped to is empty AND isn't already in our valid moves set
			# we need a set to keep track of what moves we already have so we don't go into an infinite recursion loop
			
			# Omar Al Haj: ooh yeeah keep track of my baalls baby dont overflow the stack
			if (self.board[jumpRow][jumpCol] == ".") and (not (jumpRow, jumpCol) in currValidMoves):
				# add the move to our set
				currValidMoves.add((jumpRow, jumpCol))
				# recurse
				currValidMoves = self.getValidMoveRecu(jumpRow, jumpCol, currValidMoves, True)
		return currValidMoves

	def piecesInGoalReigon(self, player):
		countInGoal = 0
		if player == self.AI:
			start = 9
			end = 15
			for row in range(13, 17):
				for col in range(start, end+1, 2):
					if self.getBall(row, col) == player:
						countInGoal += 1
				start += 1
				end -= 1
			
		else:
			start = 12
			end = 12
			for row in range(4):
				for col in range(start, end+1, 2):
					if self.getBall(row, col) == player:
						countInGoal += 1
				start -= 1
				end += 1
		
		return countInGoal

	def is_win(self, player):
		count = 0
		if player == self.Human:
			start_index = 12
			end_index = 12
			for row in range(4):
				for col in range(start_index, end_index + 1, 2):
					if self.board[row][col] == player:
						count += 1
				start_index -= 1
				end_index += 1

		else:
			start_index = 9
			end_index = 15
			for row in range(13, 17):
				for col in range(start_index, end_index + 1, 2):
					if self.board[row][col] == player:
						count += 1

				start_index += 1
				end_index -= 1

		return count == 10

	def printBoardScore(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.getBall(i, j) == " ":
					print(" ", end = " ")
				else:
					print(self.manhattan_distance([i, j], [16, 12]), end=" ")
			print("\n")

	def getNonWinningPieces(self, player):
		pieces = []
		if player == self.AI:
			for row in range(13):
				for col in range(self.cols):
					if self.getBall(row, col) == player:
						pieces.append([row, col])
		else:
			for row in range(4, 17):
				for col in range(self.cols):
					if self.getBall(row, col) == player:
						pieces.append([row, col])
		
		return pieces


	def getPlayerBalls(self, player):
		player_balls_position = []
		for row in range(self.rows):
			for col in range(self.cols):
				if self.board[row][col] == player:
					player_balls_position.append([row, col])
				if len(player_balls_position) == 10:
					return player_balls_position


	def getBall(self, row, col):
		return self.board[row][col]

