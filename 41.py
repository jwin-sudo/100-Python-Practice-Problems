'''
Exercise 41 - Letters in File

Question: Create a script that generates a text file with all letters of the English alphabet inside it, one letter per line.
'''

import string

with open("alphabet.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")
        
