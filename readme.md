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

Here, you can:
- Give your name, and choose to play my Python version of Hangman
    - Your name will be stored and referred back throughout the game so that you feel welcome and it's personalised
    - This also ties in with the file handling, and keeping track of scores
- Guess the letters in a given mystery word
- Mystery word will be randomly selected from a very big list of words
- Colours and a few sassy comments scattered throughout game to keep you entertained
- 

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

        First, we need to create a 'virtual environment'. To do this, we type the following in our terminal:
            python3 -m venv src/hangman-venv
        Now that it's created a nice little virtual environment for us to play in, we need to activate it (or 'move into' it). You can copy this text into the terminal:
            source src/hangman-venv/bin/activate
        When you press 'enter', you should be able to see (hangman-venv) at the beginning of your command line/terminal prompt, and you know you're in the right place!