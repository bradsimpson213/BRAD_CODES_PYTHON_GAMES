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
        """method to handle human input and save the move to the board"""
        print(instructions, end="")
        while True:
            try:
                play_loc = (int(input(f"Player {self.player_turn} '{'X' if self.player_turn == 1 else 'O'}' enter a number 1-9 to make your move: ")) - 1)

            except TypeError:
                print(f"You entered {play_loc}, please enter a number 1-9")
                continue

            except ValueError:
                print(f"You entered {play_loc}, please enter a number 1-9")
                continue

            else:
                if play_loc not in range(0, 10):
                    print(f"You entered {play_loc}, please enter a number 1-9") 
                    continue

                elif self.board[play_loc] != " ":
                    print(f"{self.board[play_loc]} has already played in the space, try again!")
                    continue

                else:
                    self.board[play_loc] = 'X' if self.player_turn == 1 else 'O'
                    return


    def computer_move(self):
        pass


    def minimax(self):
        pass



    def check_for_win(self):
        pass


    def play_game(self):
        pass



TicTacToe()