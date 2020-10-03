### telebot.py start ###
from cred import TOKEN, correct_chat_id
import telepot
import time
from telepot.loop import MessageLoop
from telepot.delegate import per_chat_id, create_open, pave_event_space
from pprint import pprint
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from selenium import webdriver
from single import single
from guest import guest

# matthias = guest("Matthias", "Maile", correct_chat_id)
# matthias.set_street("Eichholzstraße")
# matthias.set_street_number(57)
# matthias.set_city("Dortmund")
# matthias.set_plz(44289)
# matthias.set_phonenumber("01774772392")
#
# guestList = []
# guestList.append(matthias)

"""
### setting up the telegram bot with telepot ###
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    # pprint(msg)

    keyboard_person_amount = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Alleine', callback_data='alone')],
            [InlineKeyboardButton(text='Zu zweit', callback_data='group')],
        ])

    # iterate through list of known guests for guest data
    current_guest = None
    for potential_guest in guestList:
        if potential_guest.check_chat_id(chat_id):
            current_guest = potential_guest

    # if it is a new guest
    if current_guest == None:



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
"""

class booker(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(booker, self).__init__(*args, **kwargs)
        # the telebot starts with an empty guest list
        self.guestList = []

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        msgtext = msg['text']
        # print(chat_id)

        # check if guest is on the list
        current_guest = None
        for person in self.guestList:
            if person.check_chat_id(chat_id):
                current_guest = person
                break # stop iteration when guest is found

        # when it is a new guest
        if current_guest == None: # completely new
            current_guest = guest(chat_id)
            self.guestList.append(current_guest)
            self.sender.sendMessage('What\'s you first name?')
            return

        if current_guest.state == 10: # new guest, he send his name now
            current_guest.set_first_name(msg['text'])
            print("New guest " + msg["text"] + " added to guestList")
            current_guest.set_state(0) # user is inactive now
            self.sender.sendMessage('Hello ' + current_guest.first_name)
            return

        # checking the commands (adress, name, etc.)
        if msgtext.startswith('/plz'):
            new_plz = msgtext[5:]
            current_guest.set_plz(new_plz)
            self.sender.sendMessage('New PLZ set')




bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, booker, timeout=10),
])
MessageLoop(bot).run_as_thread()
print('Listening...')

while 1:
    time.sleep(10)

### telebot.py end ###
