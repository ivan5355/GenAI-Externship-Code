# Task 1
# Task 1 - Variables: Your First Python Intro
# Let’s start simple! Imagine you’re describing yourself (or anyone else you like) using Python variables.

# Create a name variable that stores a string (like your name or a fictional character’s name).
# Create an age variable that stores an integer value.
# Create a height variable that stores a floating-point number.

name = "Ivan"
age = 22
height = 6.5

print("Hi, my name is",name,". I am", age,"and am",height,"feet tall.")
# Task 2 - Operators: Playing with Numbers
# We all love some math, don’t we? Okay, maybe not everyone, but trust me, this will be easy and fun!

# Pick two numbers, let’s say num1 and num2 (you choose the values!).
# Perform the following operations on these numbers:
# Addition
# Subtraction
# Multiplication
# Division
# Write your Python code to calculate and display the results with a nice message for each.

num1 = 9
num2 = 4

#adding
print("Sum:",num1+num2)

#subraction
print("subtraction of 9 and 4", num1-num2)

#Multiplication
print("Multiplication of 9 and 4",num1*num2)

#Division
print("Division of 9 and 4",num1/num2)

# Task 3 - Conditional Statements: The Number Checker
# Now for the real challenge: let’s make your code think!

# Write a program that takes a number from the user and tells them whether it’s positive, negative, or zero.
# Here’s how it should work:

# Ask the user to enter a number (use the input() function).
# Use if, elif, and else statements to check:
# If the number is greater than 0, print: "This number is positive. Awesome!"
# If the number is less than 0, print: "This number is negative. Better luck next time!"
# If the number is exactly 0, print: "Zero it is. A perfect balance!"
# Make sure to test your code with a few different numbers. You’ll be surprised how fun it is to see your program come to life! 

user_input = int(input("Enter a number "))

if user_input>0:
    print("This number is positive. Awesome")
elif user_input<0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")



