"""
Instructions
Write a Python program that asks the user to enter a password and checks whether
it meets the minimum length requirement.
Requirements:
1. Ask the user to enter a password.
2. If the password contains at least 8 characters, print "Password accepted".
3. Otherwise, print "Password too short".
"""

password = input("Please enter your password ")

password_length = len(password)

if password_length >= 8:
    print("Password accepted")
else:
    print("Password too short")
