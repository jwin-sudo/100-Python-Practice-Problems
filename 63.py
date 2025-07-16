'''
Exercise 63 - Progressive Time Printer with Threshold

Question: Create a program that, once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.

Expected output: 

Hello
Hello
Hello
Hello
End of Loop
'''

import time

delay = 0

while True:
    print("Hello")
    time.sleep(delay)
    delay += 1
    if delay > 3:
        print("End of loop")
        break
