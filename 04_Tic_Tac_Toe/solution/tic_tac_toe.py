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


    def set_player_type(self, player_num):
        """Method set up if a player is human or computer"""  
        while True:
            user_input = input(f"Is Player {player_num} a Human or Computer? (enter H or C): ").upper() 
            if user_input == "H":
                return "Human"
            elif user_input == "C":
                return "Computer"
            else:
                os.system("cls")
                print(f"Incorrect input of '{user_input}', try again!")

                
    
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