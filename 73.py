'''
read this file http://www.pythonhow.com/data/sampledata.txt then multiply every values by two then export into a new txt file
'''

import pandas
 
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data * 2
data_2.to_csv("sampledata_x_2.txt", index=None)