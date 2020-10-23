#!/bin/bash
# script launching the telegram bot with selenium in the path

python3 telebot_cleaner.py
export PATH=$PATH:./
python3 telebot.py
