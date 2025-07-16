'''
Exercise 80: Solution



Exercise for reference: 

Create a program that asks the user to enter a new password and check that the submitted password should contain at least one number, one uppercase letter, and at least 5 characters. If the conditions are met, print out the reason why pointing to the specific condition/s that has not been satisfied.
'''


while True:
    psw = input("Enter password: ")

    if not any(x.isdigit() for x in psw):
        print("Must have one number")
        continue
    if not any(x.upper() for x in psw):
        print("Must have one uppercase")
        continue
    if len(psw) <5:
        print("Must have at least 5 characters")
        continue
    else:
        print("Password is fine")
        break

