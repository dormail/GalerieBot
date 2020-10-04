# testing script for the guest class
from cred import TOKEN, correct_chat_id
from guest import Guest

max = Guest(1)
max.set_first_name('max')
peter = Guest(2)
peter.set_first_name('peter')
peter.set_last_name('furlan')
tom = Guest(213)
tom.set_first_name('tom')

guestList = []
guestList.append(peter)
guestList.append(tom)
guestList.append(max)

# sort list bei chat_id of the guest
import operator
guestList.sort(key=operator.attrgetter('chat_id'))

for person in guestList:
    if person.first_name == 'peter':
        print(person.last_name)

peter.set_last_name('Lustig')

for person in guestList:
    if person.first_name == 'peter':
        print(person.last_name)
