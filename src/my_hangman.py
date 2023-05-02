import csv
import random
from colored import fg, bg, attr
from hanging_man import hanging
import __main__
# from words import potential_words

scores_file = "src/scores.csv"
wins = 0
losses = 0

# Check if there's a scores file yet
# NOTE: file_name (in video) = scores (in my code)
try:
    scores = open(scores_file, "r")
    scores.close()
    print("In try block")

except FileNotFoundError:
    scores = open(scores_file, "w")
    scores.write("name,wins,losses\n")
    scores.close
    print("In except block")

def intro(scores_file):
    global name
    name = input("Helllllo there, what's your name? ")
    global wins 
    wins = 0
    global losses
    losses = 0
    print(f"Cool {name}, let's play Python Hangman and save this fella!")
    print("_____________________________________________")
    with open(scores_file, "w") as scores:
        writer = csv.writer(scores)
        writer.writerow([name, wins, losses])

def hangman_game():
    potential_words = [
        "hello",
        "bye",
        "lamp",
    ]
    mystery_word = random.choice(potential_words).upper()
    global chances 
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

def outcome(scores_file, chances, losses, wins):
    if chances == 0:
        losses += 1
        with open(scores_file, "a") as scores:
            writer = csv.writer(scores)
            writer.writerow([name, wins, losses])
    else:
        wins += 1
        with open(scores_file, "a") as scores:
            writer = csv.writer(scores)
            writer.writerow([name, wins, losses])

# def play_again():


intro(scores_file)
hangman_game()
outcome(scores_file, chances, losses, wins)

# if __name__ == "__main__":
    # intro(scores_file)
    # hangman_game()
    # outcome(scores_file, chances, losses, wins)