# guest.py start
# eine Klasse die den Galerie Gast mit den Daten fuer die Reservierung abbildet
# fuer den Telegram Bot wird die chat_id mit gespeichert
from single import single
from selenium import webdriver

class guest:
    def __init__(self, chat_id):
        self.first_name = None
        self.last_name = None
        self.code = None
        self.street = None
        self.street_number = None
        self.city = None
        self.plz = None
        self.phonenumber = None
        self.chat_id =chat_id

    # setter methods
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_code(self, code):
        self.code = code

    # other set methods
    def set_street(self, street):
        self.street = street

    def set_street_number(self, street_number):
        self.street_number = street_number

    def set_city(self, city):
        self.city = city

    def set_plz(self, plz):
        self.plz = plz

    def set_phonenumber(self, phonenumber):
        self.phonenumber = phonenumber

    def print_adress(self):
        print(str(self.street))

    def book_single(self):
        driver = webdriver.Firefox()
        self.message = single(driver, self)
        driver.close()

    def check_chat_id(self, check_id):
        # a method which checks if the chat_id from the guest match with
        # another one
        if check_id == self.chat_id:
            return True
        else:
            return False

# guest.py end 
