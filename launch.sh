#!/bin/bash
# script launching the telegram bot with selenium in the path

python telebot_cleaner.py
export PATH=$PATH:./
python telebot.py