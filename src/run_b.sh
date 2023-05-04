#!/bin/bash

#check if python is installed

#check if venv already exists or not

python3 -m venv src/hangman-venv
source src/hangman-venv/bin/activate
pip3 install -r src/requirements.txt
clear
python3 src/draft_hangman.py
