### telebot.py start ###
from cred import TOKEN, correct_chat_id
import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    pprint(content_type)

    keyboard_person_amount = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Alleine', callback_data='alone')],
            [InlineKeyboardButton(text='Zu zweit', callback_data='group')],
        ])

    # checking for the correct username
    if chat_id != correct_chat_id:
        bot.sendMessage(chat_id, 'Bad chat_id')
        return

    # note: msg['text'] liesst nachricht aus
    bot.sendMessage(chat_id, 
            'Hallo Matthias, bist du alleine oder sollen zwei Plätze reserviert werden?',
            reply_markup=keyboard_person_amount)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

print('Listening...')

while 1:
    time.sleep(10)

### telebot.py end ###
