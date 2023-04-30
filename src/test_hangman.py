import random
import string
from hanging_man import hanging
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
    guessed_letters = set()
    word_letters = set(mystery_word)
    letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    while len(word_letters) > 0 and chances > 0:
        player_word = ""
        
        for letter in mystery_word:
            if letter in guessed_letters:
                player_word = player_word + letter
            else:
                player_word = player_word + "_ "

        print(f"\nThis is our mystery word so far: {fg(117)}{player_word}{attr(0)}")
        print("Pssst: these are the other letters you've already guessed: ", " ".join(guessed_letters))
        guess = input("\nWhat letter do you want to try? \n").upper()


        if guess in letters - guessed_letters: #ie. still in alphabet, minus the ones we've tried
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                chances = chances - 1
                print(hanging[chances])

        elif guess in guessed_letters:
            print(f"You already tried {guess}, so let's go with a different letter.")
        else:
            print(f"Come on, {guess} isn't a letter, you're gunna have to give it another go.")
            
    if chances == 0:
        print(f"\nThe word was {fg(196)}{mystery_word}{attr(0)}. Better luck next time!")
    else:
        print(f"Nice! You figured out the word is {fg(117)}{mystery_word}{attr(0)}, won Python Hangman, and saved the man!")


# name = input("Hi, what's your name? ")
# print(f"Hey {name}, let's play Python Hangman!")
print("_________________________________")
hangman_game()