'''
Exercise 36 - Word Counter

Question: Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.

Expected output:

10 
'''

def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return len(text.split())

result = count_words_in_file('words1.txt')
print(result)