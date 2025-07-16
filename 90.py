'''
extra data from database.db then export to csv file
'''

import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor() 
cur.execute('SELECT country FROM countries WHERE area >= 2000000')
rows = cur.fetchall()
conn.close()



with open("countries_large_area.csv", "w") as file:
    for i in rows:
        file.write(i[0] + "\n")