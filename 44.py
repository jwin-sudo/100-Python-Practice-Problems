'''
Exercise 44 - Letters Three by Three

Question: Create a script that generates a file where all letters of the English alphabet are listed three in each line. The inside of the text file would look like:

abc
def
ghi

and so on.
'''

import string

with open("alphabet3.txt", "w") as file:
    for letter1, letter2, letter3 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2], string.ascii_lowercase[2::2]):
        file.write(letter1 + letter2 + letter3 + '\n')