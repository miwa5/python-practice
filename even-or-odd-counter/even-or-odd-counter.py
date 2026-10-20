"""
Write a Python program that asks the user for a positive integer and prints all the even numbers from 1 up to that number.

At the end, the program should also print how many even numbers were found.
"""

chosen_number = int(input("Enter a positive integer: "))

numbers = range(1,chosen_number+1)

even_count = 0
for number in numbers:
    if number % 2 == 0:
        print (number)
        even_count += 1

print(even_count)
