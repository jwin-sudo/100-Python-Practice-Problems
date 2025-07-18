'''
Exercise 83 - Monitor Size Detector

Question: Write a script that detects and prints out your monitor resolution.

Expected output: 

Width: 1920,  Height: 1080
'''

from screeninfo import get_monitors
 
width=get_monitors()[0].width
height=get_monitors()[0].height
 
print("Width: %s,  Height: %s" % (width, height))