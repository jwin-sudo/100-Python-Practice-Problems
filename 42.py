'''
Exercise 42 - Iterating Multiple Sequences

Question: Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)

Expected output: 

5
7
9
'''

a = [1, 2, 3]
b = (4, 5, 6)

for x, y in zip(a, b):
    print(x + y)