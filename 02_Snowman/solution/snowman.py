from random  import choice
from logo import logo
from stages import snowman
import os


def get_game_word():
    """reads in words.txt and then randomly chooses a game word"""
    with open("words.txt") as file:
        words = [word.rstrip() for word in file]
        return choice(words)


def printer(snowman, chances, display, guesses, error=None):
    """custom print function for the game"""
    if error:
        print(error)
    print(snowman[chances])
    print(" ".join((display)))    
    if guesses:
        print(f"You have guessed: {[guess.upper() for guess in guesses]}")


def handle_guess(guesses, chances, display):
    """handle user input and validating it"""
    bad_guess = True

    while bad_guess:
        guess = input("Guess a letter: ").lower()
        os.system("clear")

        if len(guess) != 1:
            error = f"We can only guess a single letter, not {guess},try again, no penalty"
            # print(snowman[chances])
            # print(" ".join((display)))
            printer(snowman, chances, display, guesses, error)
            # print(f"You have guessed: {guesses}")
            continue

        if guess not in 'abcdefghijklmnopqrstuvwxyz':
            error = f"You can only guess letters, not {guess}, try again, no penalty"
            # print(snowman[chances])
            # print(" ".join((display)))
            printer(snowman, chances, display, guesses, error)
            # print(f"You have guessed: {guesses}")
            continue
        
        if guess in guesses:
            error = f"You already guessed {guess}, try again, no penalty"
            # print(snowman[chances])
            # print(" ".join((display)))
            printer(snowman, chances, display, guesses, error)
            # print(f"You have guessed: {guesses}")
            continue

        bad_guess = False

    return guess


def play_game():
    os.system("cls")
    print(logo)
    print("Welcome to Snowman!")
    print("♫♬ DO YOU WANT TO MELT A SNOWMAN!!! ♬♫")
    print("Guess the word before the snowman melts...")
    game_word = get_game_word()
    display = ["_" for _ in range(len(game_word))]
    chances = 0
    guesses = set() 
    # print(snowman[chances])
    # print(" ".join((display)))
    printer(snowman, chances, display, guesses)

    play = True
    while play:
        guess = handle_guess(guesses, chances, display)
        guesses.add(guess)

        for index, letter in enumerate(game_word):
            if letter == guess:
                display[index] = letter.upper()
        
        if guess not in game_word:
            chances += 1
            print(f"Sorry, {guess.upper()} was not in the game word...")
            if chances == 6:
                os.system("cls")
                print(snowman[-1])
                play = False
                print(f"You lose! The word was {game_word.upper()}. POOR FROSTY 💧💧💧")
                return 

        # print(snowman[chances])
        # print(" ".join((display)))
        printer(snowman, chances, display, guesses)
        # print(f"You have guessed: {guesses}")

        if "_" not in display:
            play = False
            print(f"{game_word.upper()} was the word!  YOU WIN!  FROSTY LIVES! ⛄️")
            return

play_game()