import os
files = os.listdir("letters")  # Assuming the files are in a directory named 'letters'
letter = [f[0] for f in files if f.endswith(".txt") and f[0].lower() in "python"]
print(letter)