#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
    echo "Oops!
This game is called Python Hangman, so you need Python to play!
To install Python3, just go to https://www.python.org/downloads/" >&2
    exit 1
else
    echo "Looks like Python 3 is here and you're good to go!"
fi

# Now, this should print out Python 3 (with a few extra dots + numbers)

# If you get an error code, it simply means you have to upgrade/install
# Python on your system! 
# You can find details on how to do that at the link in the readme file.