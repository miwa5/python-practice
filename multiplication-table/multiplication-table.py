"""
Write a Python program that asks the user to enter an integer and prints its multiplication table from 1 to 10.
"""

number = int(input ("Choose a number "))

factors = range (1,11)

for factor in factors:
    result = number * factor
    print(f"{number} x {factor} = {result}")
