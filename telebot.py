### telebot.py start ###
from cred import TOKEN, correct_chat_id
import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pprint(chat_id)

    keyboard_person_amount = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Button1', callback_data='b1_pressed')],
            [InlineKeyboardButton(text='Button2', callback_data='b2_pressed')],
        ])

    # checking for the correct username
    if chat_id != correct_chat_id:
        bot.sendMessage(chat_id, 'Bad chat_id')
        return

    # note: msg['text'] liesst nachricht aus
    bot.sendMessage(chat_id, 'Willkommen zum GalerieBot, wie lautet der heutige Sicherheitscode?')


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

print('Listening...')

while 1:
    time.sleep(10)

### telebot.py end ###
