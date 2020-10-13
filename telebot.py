### telebot.py start ###
from cred import TOKEN
import telepot
import time
from telepot.loop import MessageLoop
from telepot.delegate import per_chat_id, create_open, pave_event_space
from selenium import webdriver
from single import single
from guest import guest
import sqlite3


# list of all the known guests
guestList = []


class booker(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(booker, self).__init__(*args, **kwargs)

    def on_chat_message(self, msg):
        # db stuff
        conn = sqlite3.connect('guests.db')
        c = conn.cursor()

        content_type, chat_type, chat_id = telepot.glance(msg)
        msgtext = msg['text']
        # print(chat_id)

        # check if guest is on the list
        current_guest = None
        for person in guestList:
            if person.check_chat_id(chat_id):
                current_guest = person
                break  # stop iteration when guest is found

        c.execute("select * from guests where chat_id=:ins", {"ins": chat_id})

        # when no guest with matching chat_id was found
        if c.fetchone() is None:
            print(str(chat_id))
            c.execute('insert into guests values (\'None\', \'None\', 0000, \'None\', 0, 0, 0, ?, 10)', (chat_id))
            print('Guest added to SQlite db')
            conn.commit()
            conn.close()
        #current_chat_id =

        # when it is a new guest
        if current_guest is None:  # completely new
            current_guest = guest(chat_id)
            guestList.append(current_guest)
            self.sender.sendMessage('What\'s you first name?')
            return

        if current_guest.state == 10:  # new guest, he send his name now
            current_guest.set_first_name(msg['text'])
            print(
                str(chat_id) + ":\t" +
                "New guest " + msg["text"] + " added to guestList"
            )
            current_guest.set_state(0)  # user is inactive now
            self.sender.sendMessage('Hello ' + current_guest.first_name)
            return

        # checking the setter commands (adress, name, etc.)
        # since this bot is for a german institution the commands are in German
        if msgtext.startswith('/vorname'):
            new_first_name = msgtext[9:]
            current_guest.set_first_name(new_first_name)
            self.sender.sendMessage('First name set to ' + new_first_name)
            return

        if msgtext.startswith('/nachname'):
            new_last_name = msgtext[10:]
            current_guest.set_last_name(new_last_name)
            self.sender.sendMessage('Last name set to ' + new_last_name)
            return

        if msgtext.startswith('/strasse'):
            new_street = msgtext[9:]
            current_guest.set_street(new_street)
            self.sender.sendMessage('Street set to ' + new_street)
            return

        if msgtext.startswith('/hausnummer'):
            new_hn = msgtext[12:]
            current_guest.set_house_number(new_hn)
            self.sender.sendMessage('Housenumber set to ' + new_hn)
            return

        if msgtext.startswith('/stadt'):
            new_city = msgtext[7:]
            current_guest.set_city(new_city)
            self.sender.sendMessage('City set to ' + new_city)
            return

        if msgtext.startswith('/plz'):
            new_plz = msgtext[5:]
            current_guest.set_plz(new_plz)
            self.sender.sendMessage('New PLZ set to ' + new_plz)
            return

        if msgtext.startswith('/code'):
            if len(msgtext) != 10:
                self.sender.sendMessage('Für den Code formatiere deine Nachricht so:\n /code 1234')
                return
            tmp = msgtext[6:]
            current_guest.set_code(tmp)
            self.sender.sendMessage('Sicherheits-Code geändert')
            return

        # giving back all the information the bot has about a user
        if msgtext.startswith('/info'):
            print(
                str(chat_id) + ":\t" +
                current_guest.first_name + ' ' +
                ' asked for his info'
            )
            message = 'The Information I currently have about you:\n'
            message = message + current_guest.first_name
            if current_guest.last_name is not None:
                message = message + ' ' + current_guest.last_name

            if current_guest.street is not None and current_guest.house_number is not None:
                message = message + '\n'
                message = message + current_guest.street + ' ' + \
                          current_guest.house_number

            if current_guest.city is not None and current_guest.plz is not None:
                message = message + '\n'
                message = message + current_guest.plz + ' ' + \
                          current_guest.city

            self.sender.sendMessage(message)
            return

        # booking a seat for your self
        if msgtext.startswith('/alleine'):
            self.sender.sendMessage('Ok, ich reserviere dir einen Platz')
            driver = webdriver.Firefox()
            single(driver, current_guest)
            time.sleep(3)
            driver.save_screenshot('screenshot.png')
            self.sender.sendPhoto(open('screenshot.png', 'rb'))
            driver.close()
            return

        # booking a chair for 2 people
        if msgtext.startswith('/zwei'):
            self.sender.sendMessage('Function not implemented yet!')
            return

        # when he did not understand
        self.sender.sendMessage('Das habe ich nicht verstanden.')


bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, booker, timeout=10),
])
print('Launching GalerieBot')
MessageLoop(bot).run_as_thread()
print('Listening to incoming messages...')

while 1:
    time.sleep(10)

# telebot.py end #
