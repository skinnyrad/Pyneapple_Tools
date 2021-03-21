#!/usr/bin/env python
import sqlite3
import os

file = open('/pineapple/Pyneapple_Tools/Activity_Log.dump','w')

con = sqlite3.connect('/tmp/log.db')

#handles errors when someone has used emoji for their SSID
con.text_factory = lambda b: b.decode(errors = 'ignore')

cursor = con.cursor()

#Select everything in the log
cursor.execute("SELECT * FROM log")
for row in cursor.fetchall():
    file.write(','.join(str(s) for s in row) + '\n')
file.close()

#formats top_ssids.txt file
os.system('cat /pineapple/Pyneapple_Tools/Activity_Log.dump | cut -c3- | sort | cut -d "," -f 1,2| uniq -c | cut -d "," -f 2 | sort | uniq -c | sort -r > /pineapple/Pyneapple_Tools/top_ssids.txt')

#outputs formatted file to screen after running
os.system('cat /pineapple/Pyneapple_Tools/top_ssids.txt')
