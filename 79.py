'''
Exercise 79:

Exercise for reference: 

Create a program that asks the user to enter a new password and check that the submitted password should contain at least one number, one uppercase letter, and at least 5 characters. If the conditions are generated, print out "Password is fine"; otherwise, keep prompting the user for a password.
'''

while True:
    password = input("Enter password: ")
    if any(i.isdigit() for i in password) and any(i.upper() for i in password) and len(password) >= 5:
           print("Password is fine")
           break
    else:
          print("Password is not fine")
    
