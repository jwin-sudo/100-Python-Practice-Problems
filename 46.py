'''
write a script to extract 26 files and print out each letter into a list 
'''


# read all the files in the letters directory and extract the letters from the filenames then put them into a list
import os
files = os.listdir("letters")  # Assuming the files are in a directory named 'letters'
letters = [f[0] for f in files if f.endswith(".txt") and f[0].lower() in "abcdefghijklmnopqrstuvwxyz"]
print(letters)  # This will print the list of letters extracted from the filenames