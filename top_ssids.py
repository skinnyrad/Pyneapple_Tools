#!/usr/bin/env python
import sqlite3
import os

file = open('/pineapple/Activity_Log.dump','w')

con = sqlite3.connect('/tmp/log.db')
cursor = con.cursor()
cursor.execute("SELECT * FROM log")
for row in cursor.fetchall():
    file.write(','.join(str(s) for s in row) + '\n')
file.close()

os.system('cat /pineapple/Activity_Log.dump | cut -c3- | sort | cut -d "," -f 1,2| uniq -c | cut -d "," -f 2 | sort | uniq -c | sort -r > top_ssids.txt')
