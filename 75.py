'''
Exercise 75: 

Exercise for reference: 

Please plot the data of this file into a graph of x and y axis.
'''

import pandas as pd
import matplotlib.pyplot as plt  # Use this instead of pylab

# Read the data from URL
data = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")

# Plot a scatter plot
data.plot(x='x', y='y', kind='scatter')

# Show the plot
plt.show()
