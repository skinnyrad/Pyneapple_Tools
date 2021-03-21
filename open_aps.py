#!/usr/bin/env python
import sqlite3
import os

file = open('/pineapple/aps.dump','w')

con = sqlite3.connect('/tmp/recon.db')
cursor = con.cursor()
cursor.execute("SELECT * FROM aps")
#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for row in cursor.fetchall():
#    print(row)
    file.write(','.join(str(s) for s in row) + '\n')
file.close()

os.system("""cat aps.dump | cut -c2- | sort | cut -d "," -f 1,2,4 | sort | uniq | grep ",0" | cut -d "," -f 2 > open_aps.txt""")
