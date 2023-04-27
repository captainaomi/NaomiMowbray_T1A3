import random
from words import potential_words

def hangman_game():

    potential_words = [
        "hello",
        "bye",
        "lamp",
        "mint"
    ]
    word = random.choice(potential_words)
    turns = 6
    guessed = ''
    letters = set('abcdefghijklmnopqrstuvwxyz') #Can I use something like .isalpha instead?

    while len(word) > 0: #should there be a space there?
        mystery_word = ""
        # incorrect = 0

        for letter in word:
            if letter in guessed:
                mystery_word = mystery_word+letter
            else:
                mystery_word = mystery_word+"_ "

        if mystery_word == word:
            print(mystery_word)
            print("You saved the man!")
            break

        print("guess the words ", mystery_word)
        guess = input()

        if guess in letters:
            guessed = guessed+guess
        else:
            print(f"\nCome on, {guess} isn't a letter.")

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("-------")
            if turns == 8:
                print("8 turns left")
                print("-------")
                print("   0   ")
            if turns == 7:
                print("7 turns left")
                print("-------")
                print("   0   ")
                print("   |   ")
            if turns == 6:
                print("6 turns left")
                print("-------")
                print("   0   ")
                print("   |   ")
                print("  /   ")
            if turns == 5:
                print("5 turns left")
                print("-------")
                print("   0   ")
                print("   |   ")
                print("  / \  ")
            if turns == 4:
                print("4 turns left")
                print("-------")
                print("  \o   ")
                print("   |   ")
                print("  / \  ")
            if turns == 3:
                print("3 turns left")
                print("-------")
                print("  \o/   ")
                print("   |   ")
                print("  / \  ")
            if turns == 2:
                print("2 turns left")
                print("-------")
                print("  \o/ |")
                print("   |   ")
                print("  / \  ")
            if turns == 1:
                print("only 1 turn left")
                print("-------")
                print("  \o/_|")
                print("   |   ")
                print("  / \  ")
            if turns == 0:
                print("you lose")
                print("-------")
                print("   o_| ")
                print("  /|\  ")
                print("  / \  ")
                break


name = input("Hi, what's your name? ")
print(f"Hey {name}, let's play Python Hangman!")
print("_________________________________")
hangman_game()