# guest.py start
# eine Klasse die den Galerie Gast mit den Daten fuer die Reservierung abbildet
# fuer den Telegram Bot wird die chat_id mit gespeichert


class Guest:
    def __init__(self, chat_id):
        self.first_name = None
        self.last_name = None
        self.code = None
        self.street = None
        self.house_number = None
        self.city = None
        self.plz = None
        self.phonenumber = None
        self.chat_id = chat_id
        self.state = 10  # new guest, so state = 10

    # setter methods
    def set_state(self, state):
        """
        :param state: the new state for the guest
            state codes:
             0 - inactive
             10 - new guest (e.g guest doesnt have a name set)
        :return: no return value
        """
        self.state = state

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_code(self, code):
        self.code = code

    # other set methods
    def set_street(self, street):
        self.street = street

    def set_house_number(self, street_number):
        self.house_number = street_number

    def set_city(self, city):
        self.city = city

    def set_plz(self, plz):
        self.plz = plz

    def set_phonenumber(self, phonenumber):
        self.phonenumber = phonenumber

    def print_adress(self):
        print(str(self.street))

    def check_chat_id(self, check_id):
        # a method which checks if the chat_id from the guest match with
        # another one
        if check_id == self.chat_id:
            return True
        else:
            return False

# guest.py end 
