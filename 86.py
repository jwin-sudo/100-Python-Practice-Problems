'''
Exercise 86 - Data Checker

Question: Please take a look at the following list:

checklist = ["Portugal", "Germany", "Munster", "Spain"]

One of the items is not a country. Please use Python and the file containing the list of countries (attached) as the data source to filter out the checklist  of non-country items. Once you have filtered out checklist , then print it out.

Expected output: 

['Germany', 'Portugal', 'Spain']

'''

checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries_cleaned.txt", "r") as file:
    countries = file.readlines()

countries = [i.strip("\n") for i in countries]

filtered_checklist = [item for item in checklist if item in countries]
print(filtered_checklist)
