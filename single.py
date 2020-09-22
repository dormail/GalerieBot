### single.py start ###
from selenium import webdriver
from guest import guest
# from selenium import Select
# from selenium import Keys

def single(driver, guest):
    # firefox als webdriver
    #driver = webdriver.Firefox()
    
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
    first_name_fill = guest.first_name
    last_name_fill = guest.last_name
    if guest.street != False:
        street_fill = guest.street
    else:
        return "Please set a street"
    if guest.plz != False:
        plz_fill = guest.plz
    else:
        return "Please set a PLZ"
    if guest.city != False:
        city_fill = guest.city
    else:
        return "Please set a City"
    phone_fill = guest.phonenumber
    #code_fill = '1234'
    if guest.code != False:
        code_fill = guest.code
    else:
        return "Please set a code"
    
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
    
    #element.find_element_by_class_name(button_class).click()
    # using the css selector
    button = driver.find_element_by_css_selector('button.' + button_class)
    button.click()

### single.py end ###
