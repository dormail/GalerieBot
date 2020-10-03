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
        if current_guest is None:  # completely new
            current_guest = guest(chat_id)
            self.guestList.append(current_guest)
            self.sender.sendMessage('What\'s you first name?')
            return

        if current_guest.state == 10: # new guest, he send his name now
            current_guest.set_first_name(msg['text'])
            print("New guest " + msg["text"] + " added to guestList")
            current_guest.set_state(0)  # user is inactive now
            self.sender.sendMessage('Hello ' + current_guest.first_name)
            return

        # checking the commands (adress, name, etc.)
        # since this bot is for a german institution the commands are in German
        if msgtext.startswith('/vorname'):
            new_first_name = msgtext[9:]
            current_guest.set_first_name(new_first_name)
            self.sender.sendMessage('First name set to ' + new_first_name)
            return

        if msgtext.startswith('/nachname'):
            new_last_name = msgtext[10:]
            current_guest.set_last_name(new_last_name)
            self.sender.sendMessage('First name set to ' + new_last_name)
            return

        if msgtext.startswith('/plz'):
            new_plz = msgtext[5:]
            current_guest.set_plz(new_plz)
            self.sender.sendMessage('New PLZ set to ' + new_plz)
            return




bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, booker, timeout=10),
])
print('Launching GalerieBot')
MessageLoop(bot).run_as_thread()
print('Listening to incoming messages...')

while 1:
    time.sleep(10)

### telebot.py end ###
