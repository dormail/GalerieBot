# guest.py start
# eine Klasse die den Galerie Gast mit seinen Daten abbildet
from single import single
from selenium import webdriver

class guest:
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.lastname = lastname
        self.code = False
        self.street = False
        self.street_number = False
        self.city = False
        self.plz = False
        self.phonenumber = False

    # setting the code the bot is going to use (each user gets his own code)
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


# guest.py end 
