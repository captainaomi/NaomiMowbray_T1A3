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

### R8 Design help documentation which includes a set of instructions which accurately describe how to use and install the application
### You must include:
#### - steps to install the application
#### - any dependencies required by the application to operate
#### - any system hardware requirements
#### - how to use any command line arguments made for the application
<br>
## Python Hangman Help 
To play our Python Hangman game, there's a long list of commands and prompts and things we could do to eventually get your computer to let you play ... However, who chooses the long way on purpose?!

I've created a couple of files that will do all it for you nice and simply - just follow the following steps:

### Getting Your Computer Ready

Firstly, you're gunna need a **computer** or a **laptop**, and an **integrated development environment** (or **IDE** for short), which is basically just a program that does fancy things with code that make you feel like you're in The Matrix! 

I strongly recommend **Visual Studio Code**, which can be downloaded here: https://code.visualstudio.com

If you already have an IDE that you prefer, then that's fine - please feel free to use that, and you should still be able to follow the below instructions to play.

Now, these instructions are based on **the average Mac user**, but they should still work if you're on Windows or Linux. If you do have any issues, please just contact me at *codernaomi@coderacademy.com.au* and my team or I will get to troubleshooting right away for you!

Ready?

Let's play!

### Getting Your Game Ready

For our **GitHub repository** (or the Matrix code that will let you play), click here: https://github.com/captainaomi/NaomiMowbray_T1A3

You should see a little green button that says **Code** - click that, and click on **Download Zip**.

Our Python Hangman game will now be in your Downloads, so double click the zip file **NaomiMowbray_T1A3-main** to unzip it 😉

There'll be a few different files and what seem like random things in there - don't worry. Even if you don't understand it all, your computer will!

Back in **Visual Studio Code**, we're going to do the following:
1. Click open folder
2. Go to Downloads, and select **NaomiMowbray_T1A3-main** and **OPEN**!
3. If Visual Studio Code asks you to trust me, click Yes - I promise I'm trustworthy

Now, you might have to open the **terminal** to do our Matrix Code stuff, so if so, type `` ^ + ` ``, which will open that for you.

First, we're going to check that you've got **Python 3** installed - otherwise, you're going to have a hard time playing our Python Hangman!

I've got the file ready to check for you, so let's run it. Please type the following in your terminal to do so:

``` py
chmod +x src/run_a.sh
source src/run_a.sh
```
If you get an `Oops!` message, visit this link to upgrade or install Python 3: https://www.python.org/downloads/ 

Once you've **Downloaded the latest version of Python 3**, simply close and reopen your Visual Studio Code program to ensure the update is correctly installed, and go back to the previous step to try this again.

If you get a `You're good to go!` message, then you're good to go!

That's pretty much it - all you have to do is run the file and guess the word to save the man 😊

To do this, type the following in your terminal:

``` py
chmod +x src/run_b.sh
source src/run_b.sh
```

### How to Actually Play

Honestly, it's pretty simple and hopefully easy for everybody to follow along!

And you should know Hangman basics... But if you don't, I got you:

#### You have to guess a mystery word letter by letter, to save a man from a brutal hanging.

#### Every wrong guess will bring him closer to his fate - it's up to you and your word guessing skills to save him!

You'll be playing in the terminal, so keep your attention there. 

And just so we're clear, when I say I want you to **type something**, I mean type it in to the terminal where the questions are - everything you type will need to be in there for the computer to know what you're telling it!

You'll be asked your name - it's kind of a friendly game (except for the poor man whose life is at stake!). Type in your **name** and hit **Enter**.

*Note: make sure you type your name exactly the same every time you play - this means being careful with captial letters too! - and your scores will be saved foor you to compete with anyone else on your computer, so just to keep track of your own scores.*

You'll have to give a **yes or no** for if you want to play or not, so go ahead and type `y` or `n` and hit **Enter**.

The game wants to help you! You can see how many letters are in the mystery word by the underscores. For example, if our word was `llama`, we'd see `_ _ _ _ _ `. 

Also, when you guess different letters, they'll show up there too as little reminders for you to refer to if you need it.

So go ahead, try your first letter, and hit **Enter**!

Let's say you went with `a`.

The word will now show as `_ _ A _ A `

Have a play, and figure out what happens if you win, lose, make an 'invalid' guess, try to repeat a letter... Have fun!

### When You're Done Playing

When you're done saving the man (or not saving him, depending on how you go!), we can exit this game really easily. 

The same *'Do you want to play?'* prompt will come up every time you either successfully guess a word or lose, so finish whatever word you're on to get some closure, and then choose `n` when you're ready for a break.

And when you want to play again next time, that's pretty easy too!

Just open up Visual Studio Code again, and open the same **NaomiMowbray_T1A3-main** folder.

This time, however, all you need to type in the terminal is:

```
source src/run_b.sh
```

and you'll be able to keep your tally going from last time!

Just remember to type your name *exactly* how you typed it the last time, to tally your score properly. If you used an alias or Captain Jack Sparrow or something and can't remember, don't stress - just follow the below instructions to look at the Score Card and jog your memory.


### Viewing Everyone's Score Tallys

You'll be able to track everyone's scores, including the **Player Name**, their **Total Wins** and **Total Losses** in the file called **scores.csv**. 

You can either view this through **Visual Studio Code**, by clicking on the file called **scores.csv** under the **src folder** on the **Explorer Panel**, or by opening the file straight from the original folder we unzipped to make this all happen! 

If you don't remember where that is, that's okay. 

You should be able to find it on your computer at **Downloads**, then **NaomiMowbray_T1A3-main**, then go into the folder called **src**, and you'll see **scores.csv** there 😊

### Have fun and enjoy saving the day with my Python Hangman game!