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