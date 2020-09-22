# guest.py start
# eine Klasse die den Galerie Gast mit seinen Daten abbildet

class guest:
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.lastname = lastname

    # setting the code the bot is going to use (each user gets his own code)
    def set_code(self, code):
        self.sec_code = code

    # other set methods
    def set_street(self, street):
        self.street = street

    def set_city(self, city):
        self.city = city


# guest.py end 
