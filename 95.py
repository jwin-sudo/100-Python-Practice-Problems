'''
Exercise 95: Solution

Exercise for reference: 

Create a program that asks the user to input values separated by commas and stores those values in a text file, each value in a separate line.
'''

input = input("Enter values separated by commas: ")
values = input.split(',')

with open('values.txt', 'w') as file:
    for value in values:
        file.write(value.strip() + '\n')

print("Values have been written to values.txt")