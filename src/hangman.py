import csv
import random

import emoji
from colored import fg, attr

from picture import hanging
from words import potential_words


file = "src/scores.csv"
scorecard = ""

try:
    with open(file, "r") as scores:
        reader = csv.DictReader(scores)
        scorecard = list(reader)

except FileNotFoundError:
    with open(file, "w", newline="") as scores:
        columns = ["Player Name", "Total Wins", "Total Losses"]
        writer = csv.DictWriter(scores, fieldnames=columns)
        writer.writeheader()


def intro(file, scorecard):
    global name
    name = input(emoji.emojize(
        "Helllllo there :clown_face: What's your name? "))
    global wins 
    wins = 0
    global losses
    losses = 0
    print("_____________________________________________")
    
    with open(file, newline="") as scores:
        columns = ["Player Name", "Total Wins", "Total Losses"]
        reader = csv.DictReader(scores, fieldnames=columns)
        scorecard = list(reader)

        return_player = False
        for row in scorecard:
            if row["Player Name"] == name:
                return_player = True
                break

        if not return_player:
            new_player = {"Player Name": name,
                          "Total Wins": wins, "Total Losses": losses}
            scorecard.append(new_player)

        with open(file, "w", newline="") as scores:
            columns = ["Player Name", "Total Wins", "Total Losses"]
            writer = csv.DictWriter(scores, fieldnames=columns)
            writer.writerows(scorecard)


def choose_mystery_word():
    # For assignment reference only: 
    # These are what I refer to in the test spreadsheet, as used
    # throughout building and testing the application:

    # potential_words = [
    #     "hello",
    #     "bye",
    #     "lamp",
    # ] 
    
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

        # The following if statement checks if our guess is still in the
        # alphabet, minus the letters we've already guessed (i.e. what
        # letters haven't we guessed yet?)
        if guess in letters - guessed: 
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
        with open(file, "r") as scores:
            reader = csv.DictReader(scores)
            scorecard = list(reader)

        for row in scorecard:
            if row["Player Name"] == name:
                row["Total Losses"] = str(int(row["Total Losses"]) + 1)

        with open(file, "w", newline="") as scores:
            columns = ["Player Name", "Total Wins", "Total Losses"]
            writer = csv.DictWriter(scores, fieldnames=columns)
            writer.writeheader()
            writer.writerows(scorecard)
    
    else:  # You won!
        with open(file, "r") as scores:
            reader = csv.DictReader(scores)
            scorecard = list(reader)

        for row in scorecard:
            if row["Player Name"] == name:
                row["Total Wins"] = str(int(row["Total Wins"]) + 1)

        with open(file, "w", newline="") as scores:
            columns = ["Player Name", "Total Wins", "Total Losses"]
            writer = csv.DictWriter(scores, fieldnames=columns)
            writer.writeheader()
            writer.writerows(scorecard)


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
            

intro(file, scorecard)
main()