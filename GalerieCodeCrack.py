# website.py start
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
# from selenium import Select
# from selenium import Keys

# firefox als webdriver
driver = webdriver.Firefox();

# namen der auszufuellenden felder
first_name = 'first_name'
last_name = 'last_name'
street = 'street'
plz = 'postal-code'
city = 'city'
phone = 'phone'
code = 'security_code'

# werte fuer die Felder
first_name_fill = 'Matthias'
last_name_fill = 'Maile'
street_fill = 'Vogelpothsweg 87'
plz_fill = '44227'
city_fill = 'Dortmund'
phone_fill = '1774772392'
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
driver.find_element_by_name(last_name).send_keys(last_name_fill)
# street adress
driver.find_element_by_name(street).send_keys(street_fill)
# plz
driver.find_element_by_name(plz).send_keys(plz_fill)
# city
driver.find_element_by_name(city).send_keys(city_fill)
# phone
driver.find_element_by_name(phone).send_keys(phone_fill)
#element = driver.find_element_by_name(code)
#element.send_keys(code_fill)

#element.find_element_by_class_name(button_class).click()
# using the css selector
for j in range(0,10000):
    i = 9999 - j
    # find code field and paste new key
    driver.find_element_by_name(code).send_keys(i)
    # click the button
    driver.find_element_by_css_selector('button.' + button_class).click()
    # when the code was correct there is no button and it will terminate
    j = i

print(j)

# website.py end
