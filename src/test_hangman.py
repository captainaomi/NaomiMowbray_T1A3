import random
import string
from hanging_man import hanging
from words import potential_words
from colored import fg, bg, attr

def hangman_game():
    # potential_words = [
    #     "hello",
    #     "bye",
    #     "lamp",
    # ]
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
        print("Pssst: as soon as you make a guess, your guesses will show here: ", " ".join(guessed_letters))
        guess = input("What letter do you want to try? ").upper()


        if guess in letters - guessed_letters: #ie. still in alphabet, minus the ones we've tried
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                chances = chances - 1
                print(hanging[chances])

        elif guess in guessed_letters:
            print(f"\nYou already tried {guess}, so let's go with a different letter.")
        else:
            print(f"\nCome on, {name}, {guess} isn't a letter, you're gunna have to give it another go.")
            
    if chances == 0:
        print(f"\nDaaaang {name}, the word was {fg(196)}{mystery_word}{attr(0)}. Better luck next time!")
    else:
        print(f"\nNice {name}, you legend! You figured out the word is {fg(117)}{mystery_word}{attr(0)}, won Python Hangman, and saved the man!")


name = input("Heyo, what's your name? ")
print(f"Cool {name}, let's play Python Hangman!")
print("_________________________________")
hangman_game()