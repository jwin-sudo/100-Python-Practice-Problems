'''
Exercise 57 - JSON to Dictionary

Question: Please download the file in the attachment and use Python to print out its content.

Expected output: 

{'employees': [{'firstName': 'John', 'lastName': 'Doe'},
               {'firstName': 'Anna', 'lastName': 'Smith'},
               {'firstName': 'Peter', 'lastName': 'Jones'}],
 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
            {'firstName': 'Jessy', 'lastName': 'Petter'}]}
'''

import json

with open("dictionary_to_json.json", "r") as file:
    content = json.loads(file.read())

print(content)