'''
Exercise 66 - Translator

Question: Create an English to Portuguese translation program.

The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

Expected output: 

Enter word: earth
terra
'''
d = dict(weather = "clima", earth = "terra", rain = "chuva") 

def english_to_portuguese(english_word):
    return d[english_word]

english_word = input("Enter word: ")
print(english_to_portuguese(english_word))
