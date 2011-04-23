from CheckerBoard import CheckerBoard
from Point import Point
from CheckersGUI import CheckersGUI
from GameState import GameState
from SquareState import SquareState
import Player

import pygtk
pygtk.require('2.0')
import gtk
import sys
import os
from gettext import gettext as _

class Checkers:

	# The Checkboard object. This stores the state of the board 
	# and contains functions for manipulating it
	board = None
	
	# The Checkerboard GUI. This displays the game to the user
	# and takes user input
	view = None

	# The last point clicked by the user
	last_clicked = None

	# The state of the game (Black's turn, paused, etc)
	state = None

	# Player objects that take turns moving against each other
	# can be AI or human
	white_player = None
	black_player = None
	

	# This method is called when the user clicks a box in the GUI. This could be called at any time,
	# including times when it is not the players turn. Any human supplied moves come through this
	# method. The moves are passed on the Human_Player objects to be validated. 
	# The widget parameter indicates where the user clicked (widget.row, widget.column) 
	def player_click(self, widget):
		# Look up that status of the cell that the user clicked from the board object
		
		cell = self.board.board[widget.column][widget.row]
			
		# This condition checks is the user is on the second click (already selected a piece
		# in their first click). This click is meant to place the piece
		if not self.last_clicked==None:
			# Look up the piece to move
			last_cell = self.board.board[self.last_clicked.column][self.last_clicked.row]
			
			# Display the old square as empty
			self.view.set_checker(self.last_clicked.row, self.last_clicked.column, "none", "none")
			
			# Display the piece in the new square
			if last_cell == SquareState.WHITE:
				self.view.set_checker(widget.row, widget.column, "regular", "white")
			elif last_cell == SquareState.WHITEKING:
				self.view.set_checker(widget.row, widget.column, "king", "white") 
			elif last_cell == SquareState.BLACK:
				self.view.set_checker(widget.row, widget.column, "regular", "black")
			elif last_cell == SquareState.BLACKKING:
				self.view.set_checker(widget.row, wodget.column, "king", "black")
			
			# Store the move into start and end points to be passed to the player
			start = self.last_clicked
			end = Point(widget.row, widget.column)	

			# Listen for next move
			self.last_clicked = None
			if self.state.get_state() == GameState.WhitesTurn and isinstance(self.white_player, Player.Human_Player):
				return_code = self.white_player.turn(start, end, self.board)
				if return_code == Player.TURN_COMPLETE or return_code == Player.JUMP_AVAILABLE:
					self.state.set_state(GameState.BlacksTurn)

				# TODO: Send messages for invalid moves or jumps available
			elif self.state.get_state() == GameState.BlacksTurn and isinstance(self.black_player, Player.Human_Player):
				return_code = self.black_player.turn(start, end, self.board) 
				if return_code == Player.TURN_COMPLETE or return_code == Player.JUMP_AVAILABLE:
					self.state.set_state(GameState.WhitesTurn)

		# If we are here this is the first click. The user is selecting  a piece to move. Only 
		# allow them to select their own pieces. Otherwise ignore the click
		elif self.state.get_state() == GameState.WhitesTurn and isinstance(self.white_player, Player.Human_Player):
			if cell == SquareState.WHITE:
				# Highlight the clicked spot and store it in the last_clicked field
				self.view.set_checker(widget.row, widget.column, "highlight_regular", "white")
				self.last_clicked = Point(widget.row, widget.column)
			elif cell == SquareState.WHITEKING:
				self.view.set_checker(widget.row, widget.column, "highlight_king", "white")
				self.last_clicked = Point(widget.row, widget.column)

		elif self.state.get_state() == GameState.BlacksTurn and isinstance(self.black_player, Player.Human_Player):
			if cell == SquareState.BLACK:
				self.view.set_checker(widget.row, widget.column, "highlight_regular", "black")
				self.last_clicked = Point(widget.row, widget.column)
			if cell == SquareState.BLACKKING: 
				self.view.set_checker(widget.row, widget.column, "hilight_king", "black")
				self.last_clicked = Point(widget.row, widget.column)
	
		
	def main(self):
		gtk.main()

	def __init__(self):
		self.board = CheckerBoard()
		self.view = CheckersGUI(self)
		self.state = GameState(GameState.WhitesTurn)
		self.white_player = Player.Human_Player(Player.WHITE)
		self.black_player = Player.Human_Player(Player.BLACK)

if __name__ == "__main__":
	checkers = Checkers()
	checkers.main()
