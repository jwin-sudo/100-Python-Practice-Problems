'''
Exercise 14 - Removing Duplicates

Question: Complete the script so that it removes duplicate items from the list a .

a = ["1", 1, "1", 2]
Expected output: 

  ['1', 2, 1] 
'''

a = ["1", 1, "1", 2]
""" solution 1
print(list(set(a)))
"""

""" solution 2
from collections import OrderedDict
print(list(OrderedDict.fromkeys(a)))
"""

# solution 3
a = ["1", 1, "1", 2]
b = []

for i in a:
    if i not in b:
        b.append(i)
print(b)
