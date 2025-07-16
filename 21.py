'''
Exercise 21 - Dictionary Filtering

Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}
Expected output: 

{'a': 1}  
'''
d = {"a": 1, "b": 2, "c": 3}

print([(key, value) for key, value in d.items() if value <= 1])