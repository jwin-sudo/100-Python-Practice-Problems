'''
Exercise 37 - Advanced Word Counter

Question: Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that a comma can separate some words with no space. For example, "Hi, it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.
'''

def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        text = text.replace(',', ' ')
    return len(text.split())

result =count_words_in_file('words2.txt')
print(result)