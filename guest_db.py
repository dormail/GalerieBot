""" guest_db.py
a script which creates the data base and table to store the guest class
"""

import sqlite3

conn = sqlite3.connect('guests.db')
c = conn.cursor()

# deleting existing database
c.execute('''DROP TABLE guests''')

c.execute('''CREATE TABLE guests
                (first_name text, last_name text, code INTEGER, street text, house_number INTEGER, plz INTEGER, phonenumber INTEGER, chat_id BIGINT)''')

conn.commit()
conn.close()