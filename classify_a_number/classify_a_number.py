"""
Create a variable called `number`. Print 'positive' if it is greater than zero,
'negative' if it is less than zero, and 'zero' if it equals zero.
"""

number = int(input("What is the number? "))


if number > 0:
    print ("positive")
elif number < 0:
    print ("negative")
else:
    print ("zero")
