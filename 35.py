'''
Exercise 35 - String Splitter

Question: Create a function that takes any string as input and returns the number of words for that string.
'''

def wordsCount(string):
    return len(string.split())

print(wordsCount("hello world"))