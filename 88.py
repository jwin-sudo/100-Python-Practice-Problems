'''
Exercise 88 - Data Filter

Question: Create a script that uses the attached countries_by_area.txt  file as data source and prints out the top 5 most densely populated countries

Expected output: 

India
Pakistan
Nigeria
China
Indonesia
'''

import pandas
 
data = pandas.read_csv("countries_by_area.txt")
data["density"] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by="density", ascending=False)
 
for index, row in data[:5].iterrows():
    print(row["country"])
