# Notes
# 1. user input
# 2. loop
# 3. number of guesses
# 4. generate a random number 
# 5. conditionals
# 6. helper function?

from random import randint


def guess(start, end):
    bad_guess = True

    while bad_guess:
        try:
            user_guess = int(input(f"Pick a number from {start} to {end}: "))

        except ValueError:
            print("We need to enter number digits only, no letters!")
            continue

        else:
            if user_guess < start or user_guess > end:
                print(f"Numbers need to be between {start} and {end}")
                continue

        bad_guess = False

    return user_guess


def guessing_game(start, end): 
    print("Welcome to the guessing game!")
    winning_number = randint(start, end)
    # print(winning_number)
    guesses = 5

    while guesses > 0:
        # commenting out the original input call for our helper function instead
        # user_guess = int(input(f"Pick a number from {start} to {end}: "))
        user_guess = guess(start, end)
        guesses -= 1

        if user_guess == winning_number:
            print(f"You guessed correct!  The number was {winning_number}, you win!")
            return

        elif user_guess > winning_number:
            print(F"You guessed too high! Try again, you have {guesses} left")

        else:
            print(f"You guessed too low!  Try again, you have {guesses} left") 
        
    print(f"You are out of guesses. Sorry you lose.  The winning number was {winning_number}")


guessing_game(1, 20)


