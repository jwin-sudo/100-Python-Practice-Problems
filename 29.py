'''
Exercise 29 - Liquid Volume Calculator

Question:  Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.


You can then test your solution by passing 2 for h and you should get the expected output.

Expected output:

4071.5040790523717
'''
import math
def calculate_liquid_volume(h, r=10):
    volume = ((4 * math.pi * r**3)/3) - ((math.pi * h**2 * (3 * r - h)) / 3)
    return volume

result = calculate_liquid_volume(2)
print(result)
