#!/usr/bin/env python
import sqlite3
import os

#create file to dump database contents
file = open('/pineapple/Pyneapple_Tools/aps.dump','w')

#create connection to database
con = sqlite3.connect('/root/recon.db')

#handles error when people use emoji for APs
con.text_factory = lambda b: b.decode(errors = 'ignore')

cursor = con.cursor()

#select all APs with no encryption
cursor.execute("SELECT * FROM aps WHERE encryption=0")

#fetch the selected entries and throw them in the dump file
for row in cursor.fetchall():
    file.write(','.join(str(s) for s in row) + '\n')
file.close()

#format the dump file to only contain a list
os.system("""cat /pineapple/Pyneapple_Tools/aps.dump | cut -d "," -f 2 | sort | uniq > /pineapple/Pyneapple_Tools/open_aps.txt""")

#display output to screen
os.system("cat /pineapple/Pyneapple_Tools/open_aps.txt")
