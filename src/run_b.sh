#!/bin/bash

python3 -m venv src/hangman-venv
source src/hangman-venv/bin/activate
pip3 install -r src/requirements.txt
clear
python3 src/hangman.py
clear
deactivate