"""
Write a program that asks the user to enter a grade between 0 and 100 and prints the corresponding letter grade.
Requirements:
- If the grade is greater than or equal to 90, print "A".
- If the grade is greater than or equal to 80, print "B".
- If the grade is greater than or equal to 70, print "C".
- If the grade is below 70, print "F"

Challenge: What happens if the user enters 150 or -10?
Modify your program to reject grades outside the range of 0 to 100.
"""

grade = int(input("Input a grade between 0 and 100 "))

if grade > 100 or grade < 0:
    print("number not valid")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
