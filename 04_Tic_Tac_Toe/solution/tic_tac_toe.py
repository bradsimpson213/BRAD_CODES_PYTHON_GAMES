import os
from time import sleep
from logo import logo, instructions
from display import print_display


class TicTacToe:
    """Class that creates instances of the Tic Tac Toe game"""

    def __init__(self):
        """Constructor to set up the game"""
        self.board = [" ", " ", " ", 
                      " ", " ", " ", 
                      " ", " ", " "]
        self.player1 = None
        self.player2 = None
        self.player_turn = 1
        self.play_game()


    def set_player_type(self):
        pass   

    
    def human_move(self):
        pass


    def computer_move(self):
        pass


    def minimax(self):
        pass



    def check_for_win(self):
        pass


    def play_game(self):
        pass



TicTacToe()