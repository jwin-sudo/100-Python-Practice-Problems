'''
Exercise 68 - User Friendly Translator

Question: Create an English to Portuguese translation program.

The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. Also, return the message, "We couldn't find that word!" when the user enters a word that is not in the dictionary. Also, make the program non-case-sensitive, meaning that, for example, both earth and Earth should return the translation correctly for that word.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

Expected output: 

Enter word: hello
We couldn't find that word!
'''

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

word = input("Enter word: ").lower()

def english_to_portuguese(word):
    try:
        if word in d.keys():
            return d[word]
    except:
        return "We couldn't find that word!"

print(english_to_portuguese(word))