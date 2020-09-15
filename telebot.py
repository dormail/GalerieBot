### telebot.py start ###
from cred import TOKEN
import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pprint(msg['chat']['first_name'] + ' wrote ' + msg['text'])

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Button1', callback_data='b1_pressed')],
            [InlineKeyboardButton(text='Button2', callback_data='b2_pressed')],
        ])

    bot.sendMessage(chat_id, 'What are those buttons', reply_markup=keyboard)

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

print('Listening...')

while 1:
    time.sleep(10)

### telebot.py end ###
