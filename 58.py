'''
Exercise 58 - Add to JSON

Question: Please download the json file in the attachment and use Python to add a new employee to the file's content so that the file looks like in the expected output below.

Expected output: 
'''

import json
from pprint import pprint
with open("dictionary_to_json.json", "r") as file:
    content = json.loads(file.read())
    

content["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
pprint(content)