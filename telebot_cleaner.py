""" telebot_cleaner.py start
a python script which opens a telegram bot session so all messages are marked
as read
"""
import time
from cred import TOKEN
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import per_chat_id, create_open, pave_event_space
from pprint import pprint
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

class cleaner(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(cleaner, self).__init__(*args, **kwargs)
        # the telebot starts with an empty guest list

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        msgtext = msg['text']
        print(
            str(chat_id) +
            ' wrote ' +
            msg['text']
        )


print('Unread messages:')
bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, cleaner, timeout=10),
])
MessageLoop(bot).run_as_thread()

time.sleep(3)

print('All messages marked as read')

### telebot_cleaner.py end ###
