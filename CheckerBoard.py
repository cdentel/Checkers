from SquareState import SquareState

class CheckerBoard:
	board = []
	def __init__(self):
	#All initialization
		for col in range(8):
			self.board.append([])
			for row in range(8):
				if row < 3 and (col + row) % 2 == 1:
					self.board[col].append(SquareState.BLACK)
				elif row > 4 and (col + row) % 2 == 1:
					self.board[col].append(SquareState.WHITE)
				else:
					self.board[col].append(SquareState.EMPTY)
		

		
	"""
	This method is used for printing the board in ascii. It is only useful until the GUI is built.
	Remove for production
	"""     	
	def printBoard(self): 	
		result = "|---|---|---|---|---|---|---|---|\n"
		for row in range(len(self.board)): 	
			for col in range(len(self.board[0])):
				result += "|" + SquareState.printSquare(self.board[col][row],(row+col)%2==0)
			result +="|\n|---|---|---|---|---|---|---|---|\n"
		print result


	# Returns whether or not the game is over 
	def gameOver(whoseTurn):
		if getAllMoves(whoseTurn) == None:
			return True
		return False
    	
	
	# Returns the colorInt of the winner (-1 if game not over)
	# Input is the color of the player who most recently had a turn
	def gameWinner(whoseTurnLast):
		return Player.WHITE
	
	# Checks to see if the given move is legal.  
	# Inputs are two Point objects: the start point and the end point
	# Pre: 1)start and end are points in the 8*8 board 2)GameState.get_state() is 1 or 2 (either player is playing)
	def checkMove(self, start, end):
		if start.x%2 + start.y%2 != 1 or end.x%2 + end.y%2 !=1:
			return False

		if not self.board[start.x][start.y] == GameState.get_state()*2-1 or not self.board[end.x][end.y] == SquareState.EMPTY:
			return False

		if end.y - start.y == abs(end.y - start.y)*(GameState.get_state()*2-3) and not SquareState(start) == 2 and not SquareState(start) == 4:
			return False

		if abs(end.y - start.y) == 1 and abs(end.x - start.x) == 1 and not anyJump(GameState.get_state()):
			return True

		if abs(end.y - start.y) == 2 and abs(end.x - start.x) == 2 and self.board[(start.x + end.x)/2][(start.y + end.y)/2] == 3 - GameState.get_state():
			return True
    		return False

	# Makes the given move.  Returns true if the player has another move, else false
	# Inputs are two point objects: the start point and the end point
	def move(self, start, end):
		self.board[end.column][end.row] = self.board[start.column][start.row]
		self.board[start.column][start.row] = SquareState.EMPTY
		#if anyJump():
		#	return True
		return True
	
	# Returns a list of all available Points that can be moved to from Start
	# Input is a point object
	def getMoves(start):
		return None
	
	# Returns a list of all possible moves this player can make
	def getAllMoves(whoseTurn):
		return None
	
	# private function 
	# Return ture if there are any pieces that can jump
	def anyJump(self):
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				start = Point(row, col)
				step = 0
				if canJump(start, step):
					return true
		return False
    
	# private function 	
	# Return true if user can any jump from a particular start
	def canJumps(self, start):
		if step == 4:
			return False
		if start.x%2 + start.y%2 != 1 or x%2 + y%2 !=1:
			return False
		if not self.board[start.x][start.y] == GameState.get_state()*2-1:
			return False
		if step == 3:
			x = start.x + 2
			y = start.y + 2
		elif mode == 2:
			x = start.x + 2
			y = start.y - 2
		elif mode == 1:
			x = start.x - 2
			y = start.y + 2
		else:
			x = start.x - 2
			y = start.y - 2
		if x <= 7 and x >= 0 and y <= 7 and y >= 0:
			if end.y - start.y != abs(end.y - start.y)*(GameState.get_state()*2-3) or SquareState(start) == 2 or SquareState(start) == 4:
				if abs(end.y - start.y) == 2 and abs(end.x - start.x) == 2 and self.board[(start.x + end.x)/2][(start.y + end.y)/2] == 3 - GameState.get_state():
					if self.board[end.x][end.y] != SquareState.EMPTY:
						return True
		step += 1
			
			
	

	
	
