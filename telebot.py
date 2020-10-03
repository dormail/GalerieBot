### telebot.py start ###
from cred import TOKEN, correct_chat_id
import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from selenium import webdriver
from single import single
from guest import guest

matthias = guest("Matthias", "Maile", correct_chat_id)
matthias.set_street("Eichholzstraße")
matthias.set_street_number(57)
matthias.set_city("Dortmund")
matthias.set_plz(44289)
matthias.set_phonenumber("01774772392")

### setting up the telegram bot with telepot ###
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    # pprint(msg)

    keyboard_person_amount = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Alleine', callback_data='alone')],
            [InlineKeyboardButton(text='Zu zweit', callback_data='group')],
        ])

    # checking for the correct username
    # not needed in future since every user has his own chat

    ### hier werden generelle chat nachrichten ausgwertet ###
    # note: msg['text'] liesst nachricht aus
    if msg['text'] == 'Gib Tisch':
        bot.sendMessage(chat_id, 
            'Hallo Matthias, bist du alleine oder sollen zwei Plätze reserviert werden?',
            reply_markup=keyboard_person_amount)

    if len(msg['text']) == 4:
        # we are just gonna assume that its a code and that it is correct
        print("Booking for one person from " + str(chat_id) + " with the code " + msg['text'])
        bot.sendMessage(chat_id,
                'Buche einen Tisch für dich mit dem Code ' + msg['text'])
        matthias.set_code(msg['text'])
        single(webdriver.Firefox(), matthias)

def on_callback_query(msg):
    print('hi')
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    ### hier kann die antwort mit Buttons ausgewertet werden ###
    bot.answerCallbackQuery(query_id, text='Ok')

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
    'callback_query': on_callback_query}).run_as_thread()

print('Listening...')

while 1:
    time.sleep(10)

### telebot.py end ###
