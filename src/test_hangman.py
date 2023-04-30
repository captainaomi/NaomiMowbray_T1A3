import random
import string
from words import potential_words
from colored import fg, bg, attr

def hangman_game():

    potential_words = [
        "hello",
        "bye",
        "lamp",
    ]
    mystery_word = random.choice(potential_words).upper()
    chances = 9
    guessed = ""
    letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    while len(mystery_word) > 0:
        player_word = ""

        for letter in mystery_word:
            if letter in guessed:
                player_word = player_word + letter
            else:
                player_word = player_word + "_ "

        if player_word == mystery_word:
            print(f"Nice! You figured out the word is {mystery_word}, won Python Hangman, and saved the man!")
            break

        print(f"\nOkay, let's guess a letter in this mystery word: {player_word}")
        print("Pssst: these are the ones you've already guessed: ", " ".join(guessed))
        guess = input().upper()

        if guess in letters:
            if guess in guessed:
                print(f"You already tried {guess}, so let's go with a different letter.")
            guessed = guessed + guess
        else:
            print(f"Come on, {guess} isn't a letter, you're gunna have to give it another go.")

        if guess not in mystery_word:
            chances = chances - 1
            if chances == 8:
                color = bg(15) + fg(0)
                reset = attr('reset')
                print(color + "________" + reset)
                print(color + "|       " + reset)
                print(color + "|       " + reset)
                print(color + "|       " + reset)
                print(color + "|       " + reset)
                print(color + "|_______" + reset)
                print("8 turns left")
            if chances == 7:
                color = bg(227) + fg(0)
                reset = attr('reset')
                print(color + "________" + reset)
                print(color + "|   |   " + reset)
                print(color + "|       " + reset)
                print(color + "|       " + reset)
                print(color + "|       " + reset)
                print(color + "|_______" + reset)
                print("7 turns left")
            if chances == 6:
                color = bg(220) + fg(0)
                reset = attr('reset')
                print(color + "________" + reset)
                print(color + "|   |   " + reset)
                print(color + "|   o   " + reset)
                print(color + "|       " + reset)
                print(color + "|       " + reset)
                print(color + "|_______" + reset)
                print("6 turns left")
            if chances == 5:
                color = bg(214) + fg(0)
                reset = attr('reset')
                print(color + "________" + reset)
                print(color + "|   |   " + reset)
                print(color + "|   o   " + reset)
                print(color + "|   |   " + reset)
                print(color + "|       " + reset)
                print(color + "|_______" + reset)
                print("5 turns left")
            if chances == 4:
                color = bg(208) + fg(0)
                reset = attr('reset')
                print(color + "________" + reset)
                print(color + "|   |   " + reset)
                print(color + "|  \o   " + reset)
                print(color + "|   |   " + reset)
                print(color + "|       " + reset)
                print(color + "|_______" + reset)
                print("4 turns left")
            if chances == 3:
                color = bg(196) + fg(0)
                reset = attr('reset')
                print(color + "________" + reset)
                print(color + "|   |   " + reset)
                print(color + "|  \o/  " + reset)
                print(color + "|   |   " + reset)
                print(color + "|       " + reset)
                print(color + "|_______" + reset)
                print("3 turns left")
            if chances == 2:
                color = bg(88) + fg(0)
                reset = attr('reset')
                print(color + "________" + reset)
                print(color + "|   |   " + reset)
                print(color + "|  \o/  " + reset)
                print(color + "|   |   " + reset)
                print(color + "|  /    " + reset)
                print(color + "|_______" + reset)
                print("2 turns left")
            if chances == 1:
                color = fg(0) + bg(52)
                reset = attr('reset')
                print(color + "________" + reset)
                print(color + "|   |   " + reset)
                print(color + "|  \o/  " + reset)
                print(color + "|   |   " + reset)
                print(color + "|  / \  " + reset)
                print(color + "|_______" + reset)
                print("Oh gosh, you're on your last chance...")
            if chances == 0:
                color = fg(0) + bg(0)
                reset = attr('reset')
                print(color + "________" + reset)
                print(color + "|   |   " + reset)
                print(color + "|   o   " + reset)
                print(color + "|  /|\  " + reset)
                print(color + "|  / \  " + reset)
                print(color + "|_______" + reset)
                print(f'''Ba-bow, you lose (and so does our unfortunate man).
The word was {mystery_word}. Better luck next time!''')
                break


# name = input("Hi, what's your name? ")
# print(f"Hey {name}, let's play Python Hangman!")
print("_________________________________")
hangman_game()