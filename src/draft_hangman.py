import csv
import random
import emoji
from colored import fg, bg, attr
from hanging_man import hanging
import __main__
from words import potential_words

file = "src/scores.csv"
wins = 0
losses = 0
retrieved = ""

# I've been trying:
# if (name != row[0]) and variations of this but keep getting DictWriter is not iterable or callable


# try:
#     scores = open(file, "r")
#     columns = ["Player Name", "Total Wins", "Total Losses"]
#     retrieved = csv.DictReader(scores, fieldnames = columns)
#     for row in retrieved:
#         print(row)
#     scores.close()
#     print(retrieved)
#     print("In try block")

# except FileNotFoundError:
#     scores = open(file, "w")
#     columns = ["Player Name", "Total Wins", "Total Losses"]
#     retrieved = csv.DictWriter(scores, fieldnames = columns)
#     scores.close()
#     print("In except block")


def intro(file, retrieved):
    global name
    name = input(emoji.emojize(
        "Helllllo there :clown_face: What's your name? "))
    global wins 
    wins = 0
    global losses
    losses = 0
    
    print("_____________________________________________")
    # with open(file, "a", newline="") as scores:
    #     columns = ["Player Name", "Total Wins", "Total Losses"]
    #     retrieved = csv.DictWriter(scores, fieldnames = columns)
    #     retrieved.writeheader()
    #     for row in retrieved:
    #         if retrieved() != name:
    #             retrieved.writerow({name, wins, losses})
    #         else:
    #             scores.close()


def choose_mystery_word():
    potential_words = [
        "hello",
        "bye",
        "lamp",
    ] # These were used while building and testing the teminal application
     
    global mystery_word
    mystery_word = random.choice(potential_words).upper()
    global word_letters
    word_letters = set(mystery_word)


def hangman_game(mystery_word, word_letters):
    global chances 
    chances = 9
    guessed = set()
    letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    while len(word_letters) > 0 and chances > 0:
        player_word = ""
        
        for letter in mystery_word:
            if letter in guessed:
                player_word = player_word + letter
            else:
                player_word = player_word + "_ "

        print(f"\nThis is our word so far: {fg(117)}{player_word}{attr(0)}")
        print("When you make a guess, it'll show here: ", " ".join(guessed))
        guess = input("What letter do you want to try? ").upper()


        if guess in letters - guessed: 
        #ie. still in alphabet, minus the ones we've tried
            guessed.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                chances = chances - 1
                print(hanging[chances])

        elif guess in guessed:
            print(
                f"\nYou already tried {guess}. Maybe try a different letter?")
        else:
            print(emoji.emojize(
                f"""\nCome on {name}, {guess} isn't a letter :woozy_face:
Let's give that another go..."""))
            


def did_he_die(chances):
    if chances == 0:
        print(emoji.emojize(
            f"""\nDang {name}, the word was {fg(196)}{mystery_word}{attr(0)}. 
Better luck next time! :crossed_fingers:"""))
    else:
        print(emoji.emojize(
            f"""\nNice job {name}, you legend! :partying_face:
The word was {fg(117)}{mystery_word}{attr(0)} - you saved the man!"""))


def outcome(chances, losses, wins):
    if chances == 0:
        losses += 1
        # with open(file, "w", newline="") as scores:
        #     columns = ["Player Name", "Total Wins", "Total Losses"]
        #     retrieved = csv.DictWriter(scores, fieldnames = columns)
        #     retrieved.writeheader()
        # if retrieved(name) == name:
        #     retrieved.writerow({name, wins, losses})
        # else:
        #     scores.close()

    else:
        wins += 1
        # with open(file, "w", newline="") as scores:
        #     columns = ["Player Name", "Total Wins", "Total Losses"]
        #     retrieved = csv.DictWriter(scores, fieldnames = columns)
        #     retrieved.writeheader()
        # if retrieved(name) == name:
        #     retrieved.writerow({name, wins, losses})
        # else:
        #     scores.close()


def main():
    while True:
        play = input(
            f"Do you want to play Python Hangman and save this fella? (y/n) "
            ).upper()[0]
        if play == "N":
            print(emoji.emojize(
                f"No worries {name}, let's play later instead :waving_hand:"))
            break
        elif play == "Y":
            print(f"Righto {name}, let's do this!")
            choose_mystery_word()
            hangman_game(mystery_word, word_letters)
            did_he_die(chances)
            outcome(chances, losses, wins)
        else:
            print(emoji.emojize(
                "Innnnteresting, that's not a yes OR a no... :thinking_face:"))
            

intro(file, retrieved)
main()

# if __name__ == "__main__":
    # intro(scores_file)
    # hangman_game()
    # outcome(scores_file, chances, losses, wins)