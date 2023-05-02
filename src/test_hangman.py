import random
import string
from colored import fg, bg, attr
from hanging_man import hanging
from words import potential_words

def hangman_game():
    # potential_words = [
    #     "hello",
    #     "bye",
    #     "lamp",
    # ]
    mystery_word = random.choice(potential_words).upper()
    chances = 9
    guessed = set()
    word_letters = set(mystery_word)
    letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    while len(word_letters) > 0 and chances > 0:
        player_word = ""
        
        for letter in mystery_word:
            if letter in guessed:
                player_word = player_word + letter
            else:
                player_word = player_word + "_ "

        print(f"\nThis is our mystery word so far: {fg(117)}{player_word}{attr(0)}")
        print("When you make a guess, the letters will show here: ", " ".join(guessed))
        guess = input("What letter do you want to try? ").upper()


        if guess in letters - guessed: #ie. still in alphabet, minus the ones we've tried
            guessed.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                chances = chances - 1
                print(hanging[chances])

        elif guess in guessed:
            print(f"\nYou already tried {guess}, so can we try a different letter?")
        else:
            print(f"\nCome on {name}, {guess} isn't a letter, let's give that another go.")
            
    if chances == 0:
        print(f"""\nDaaaang {name}, the word was {fg(196)}{mystery_word}{attr(0)}. 
Better luck next time!""")
    else:
        print(f"""\nNice job {name}, you legend!
The word was {fg(117)}{mystery_word}{attr(0)} - you saved the man!""")


name = input("Heyo, what's your name? ")
print(f"Cool {name}, let's play Python Hangman and save this fella!")
print("_________________________________")
hangman_game()