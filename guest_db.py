""" guest_db.py
a script which creates the data base and table to store the guest class
"""

import sqlite3

conn = sqlite3.connect('guests.db')
c = conn.cursor()

# deleting existing database
c.execute('''DROP TABLE guests''')

c.execute('''CREATE TABLE guests
                (first_name , last_name , code , 
                street , house_number , plz , 
                phonenumber , chat_id , state )''')

conn.commit()
conn.close()
print("Resetting database successfull")