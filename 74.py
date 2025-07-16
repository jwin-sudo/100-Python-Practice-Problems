'''
Exercise 74 - File Concatenator

Question: Please concatenate this file with this one to a single text file. The content of the output file should look like below.

Expected output: 

x,y
3,5
4,9
6,10
7,11
8,12
6,10
8,18
12,20
14,22
16,24

'''
import pandas as pd

data1 = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pd.read_csv("sampledata_x_2.txt")

# Reset index to avoid duplicate indices in the output file
data12 = pd.concat([data1, data2], ignore_index=True)
data12.to_csv("sampledata12.txt", index=False)