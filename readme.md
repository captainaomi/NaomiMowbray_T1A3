# Naomi Mowbray T1A3 - Terminal Application

## R3 Provide full attribution to referenced sources (where applicable)

The beautiful 5,000 long list of words I utilised for my Python Hangman game can be found here: https://www.randomlists.com/data/words.json
<br>

## R4 Provide a link to your source control repository

For the **GitHub repository**, you can click here: https://github.com/captainaomi/NaomiMowbray_T1A3

<br>

## R5 Identify any code style guide or styling conventions that the application will adhere to. 
## Reference the chosen style guide appropriately.

PEP 8 is the typical style guide for Python Code, and simply works towards ensuring there's consistency across everyone's Python Code. 

Different things that I had to be careful of and learn to be congruent with included points such as:

- Limit all lines to a maximum of 79 characters, but for flowing long blocks of text with fewer structural restrictions (docstrings or comments), the line length should be limited to 72 characters

- Surround top-level function and class definitions with two blank lines, but Method definitions inside a class are surrounded by a single blank line

- Imports should be grouped in the following order:
    1. standard library imports
    2. related third party imports
    3. local application/library specific imports

You can find *Kenneth Reitz'* PEP 8 style guide here: https://pep8.org/

<br>

## R6 Develop a list of features that will be included in the application. It must include:
### - at least three features
### - describe each feature
## Note: Ensure that your features above allow you to demonstrate your understanding of the following language elements and concepts: 
### - use of variables and the concept of variable scope
### - loops and conditional control structures
### - error handling
        
Python Hangman!

Different features include:
- Give your name, and choose to play my Python version of Hangman
    - Your name will be stored and referred back throughout the game so that you feel welcome and it's personalised
    - This also ties in with the file handling, and keeping track of scores
- Guess the letters in a given mystery word
    - Kiiiinda self explanatory. 
    - `if/else` statements ensure that only alphabetical characters are used, which also negates possible errors thrown for numbers or symbols that a player might attempt to guess
- Mystery word will be randomly selected from a very big list of words, because that's how you play Hangman!
    - Letters will show as underscores if they haven't yet been guessed
    - Once correctly guessed, each correct letter will show in place of the underscore
- Chances, or lives, or 'how many more letters can you try until this guy is a goner?'
    - Nine is a good number, so I went with that. Keeps some pressure on but not impossible
    - Each wrong letter will deduct a chance
    - Each wrong letter will also print out the newest hanging man picture, as he gets closer and closer to his death
    - Numbers, symbols, multiple characters etc don't count as a wrong guess, and player is allowed to attempt that guess again with the same prompt to guess a letter
- Colours and a few sassy comments scattered throughout game to keep you entertained
    - The colours will be utilised for our mystery word and for the hanging man pictures, getting closer and closer to a black out when/if he dies
    - The choice of colours from white through to red and then black are similar to Australia's fire danger chart... Red's bad, but black's catastrophic!
`
<br>

    ## R7 Develop an implementation plan which:
    ### - outlines how each feature will be implemented and a checklist of tasks for each feature
    ### - prioritise the implementation of different features, or checklist items within a feature
    ### - provide a dealine, duration or other time indicator for each feature or checklist/checklist item
    ## Utilise a suitable project management platform to track this implementation plan
    ## Provide screnshots/images and/or a reference to an accessible project management platform used to track this implementation plan
    ## > Your checklists for each feature should have at least five items
    <br>

## R8 Design help documentation which includes a set of instructions which accurately describe how to use and install the application
## You must include:
### - steps to install the application
### - any dependencies required by the application to operate
### - any system hardware requirements
### - how to use any command line arguements made for the application

There's a long version, and there's a short version of how to play this game on your computer! 

To make things nice and simple, instead of making you type a whole lot of commands in your terminal, I've created a couple of files that will do it for you!

First, we're going to check that you've got Python 3 installed - otherwise, you're going to have a hard time playing Python Hangman!

To do this, you can type the following in your terminal:
    `python3 -m venv src/hangman-venv`
    `Enter`
Now that it's created a nice little virtual environment for you to play in, you need to activate it (or 'move into' it). You can copy this text into the terminal:
    `source src/hangman-venv/bin/activate`
    `Enter`
When you press 'enter', you should be able to see (hangman-venv) at the beginning of your command line/terminal prompt, and you'll know you're in the right place!

To make sure you've got the right requirements for the game, once you're in the venv, you just have to type: 
    `pip3 install -r src/requirements.txt` 
    `Enter`
and every requirement to run our Python Hangman game will be installed for you!


When you're done playing, you just need to type in `'no'` at the prompt to continue or stop playing the game, and then `deactivate + Enter` to leave your venv and go about your life!

Again, when those cravings kick in and you want to play again, just go back and type in:
    `source src/hangman-venv/bin/activate`
    `Enter`
Note: you won't have to install the requirements again, because they're still stored in your virtual enviornment and will be waiting for you every time you come play!