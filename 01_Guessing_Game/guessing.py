# Notes
# 1. user input
# 2. loop
# 3. number of guesses
# 4. generate a random number 
# 5. conditionals
# 6. helper function?

from random import randint


def guessing_game(start, end): 
    print("Welcome to the guessing game!")
    winning_number = randint(start, end)
    # print(winning_number)
    guesses = 5

    while guesses > 0:
        user_guess = int(input(f"Pick a numberr from {start} to {end}: "))
        guesses -= 1

        if user_guess == winning_number:
            print(f"You guessed correct!  The number was {winning_number}, you win!")
            return

        elif user_guess > winning_number:
            print(F"You guessed too high! Try again, you have {guesses} left")

        else:
            print(f"You guessed too low!  Try again, you have {guesses} left ") 
        
    print(f"You are out of guesses. Sorry you lose.  The winning number was {winning_number}")


guessing_game(1, 20)


