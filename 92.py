'''
Exercise 92 - File Counter

Question: Please download the attached ZIP file and extract its files in a folder. Then, write a script that counts and prints out the number of .py files in that folder.

Expected output: 

2
'''

import os

def count_py_files(directory):
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            count += 1  
    return count

# get from files directory here  
directory = '/Users/jamesnguyen/Desktop/Master_100_Python_Practical_Problems/files'
print(count_py_files(directory))  # Change this to your folder path