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

def is_number(password):
    for letter in password:
        if "0" <= letter <= "9":
            return True

    return False


if password_length >= 8 and is_number(password):
    print("Password accepted")
else:
    print("Password too short or missing number")
