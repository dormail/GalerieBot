""" pair.py start
booking a chair for two people
"""
from selenium import webdriver


# from selenium import Select
# from selenium import Keys

def pair(driver, guest1, guest2):
    # firefox als webdriver
    # driver = webdriver.Firefox()

    # namen der auszufuellenden felder im html code
    first_name = 'first_name'
    last_name = 'last_name'
    street = 'street'
    plz = 'postal-code'
    city = 'city'
    phone = 'phone'
    code = 'security_code'

    # werte fuer die Felder
    # immer ueberpruefen ob diese in der klasse vorhanden sind
    if guest1.first_name is not None:
        first_name_fill = guest1.first_name
    else:
        first_name_fill = 'Vorname'
    if guest1.last_name is not None:
        last_name_fill = guest1.last_name
    else:
        last_name_fill = 'Vorname'
    if guest1.street is not None:
        street_fill = guest1.street
    else:
        street_fill = 'Vorname'
    if guest1.plz is not None:
        plz_fill = guest1.plz
    else:
        plz_fill = 'Vorname'
    if guest1.city is not None:
        city_fill = guest1.city
    else:
        city_fill = 'city'
    if guest1.phonenumber is not None:
        phone_fill = guest1.phonenumber
    else:
        phone_fill = '231444444'
    # code_fill = '1234'
    if guest1.code is not None:
        code_fill = guest1.code
    else:
        code_fill = '1234'

    # weitere
    button_class = 'button.is-link.is-fullwidth.is-medium'
    url = 'https://checkin.stwdo.de/mensa/451/checkin'

    driver.get(url)

    # we are looking for the items by name
    # first name
    element = driver.find_element_by_name(first_name)
    element.send_keys(first_name_fill)
    # last name
    element = driver.find_element_by_name(last_name)
    element.send_keys(last_name_fill)
    element = driver.find_element_by_name(street)
    element.send_keys(street_fill)
    element = driver.find_element_by_name(plz)
    element.send_keys(plz_fill)
    element = driver.find_element_by_name(city)
    element.send_keys(city_fill)
    element = driver.find_element_by_name(phone)
    element.send_keys(phone_fill)
    element = driver.find_element_by_name(code)
    element.send_keys(code_fill)

    # element.find_element_by_class_name(button_class).click()
    # using the css selector
    button = driver.find_element_by_css_selector('button.' + button_class)
    button.click()

### single.py end ###
