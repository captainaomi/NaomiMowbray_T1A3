#!/bin/bash

python3 -m venv src/hangman-venv
source src/hangman-venv/bin/activate
pip3 install -r src/requirements.txt
python3 src/draft_hangman.py
