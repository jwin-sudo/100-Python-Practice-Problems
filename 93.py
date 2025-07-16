'''
Exercise 93 - Recursive File Counter

Question: Please download the attached ZIP file. Inside the ZIP file, there's a directory named subdirs. That directory contains other directories inside. Please write a script that counts the number of .py files contained inside subdirs and all its sub-directories.

Expected output: 

3

'''

import os

def count_py_files_recursive(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.py'):
                count += 1  
    return count    

# get from files directory here
directory = '/Users/jamesnguyen/Desktop/Master_100_Python_Practical_Problems/subdirs'
print(count_py_files_recursive(directory))