'''
Exercise 78

Exercise for reference: 

Create a program that generates a password of 6 random alphanumeric characters.
'''

import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

choosen = random.sample(characters, 6)
password = "".join(choosen)

print(password)