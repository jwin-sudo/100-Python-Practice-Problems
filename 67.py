'''
Exercise 67 - Advanced Translator

Question: Create an English to Portuguese translation program.

The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. In addition, try to return the message, "We couldn't find that word!" when the user enters a word that is not in the dictionary.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

Expected output: 

Enter word: hello
That word doesn't exist!
'''

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

word = input("Enter word: ")

def english_to_portuguese(word):
    if word not in d.keys():
        return "We couldn't find that word"
    return d[word]

print(english_to_portuguese(word))