'''
Exercise 72: Solution

Exercise for reference: 

Create a script that let the user type in a search term and then the program opens the browser and searches the term on Google.
'''

import webbrowser

def searchGoogle(query):
    webbrowser.open("https://google.com/search?q=%s" % query)    
    return

query = input("Enter a query: ")
print(searchGoogle(query))