'''
print today, today's date, today's year 
'''

from datetime import datetime
now = datetime.now()

print("Today is " + now.strftime("%A") + ", " + now.strftime("%Y-%m-%d") + ", " + str(now.year))