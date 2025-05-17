# Task 1 - Counting Down with Loops
# Write a Python program to create a countdown timer.

# Ask the user for a starting number.
# Use a while loop to print numbers from that number down to 1.
# When the countdown ends, print a celebratory message like "Blast off!"
# For example:

# Enter the starting number: 5
# 5 4 3 2 1 Blast off! 🚀

input1 = int(input("Enter starting number "))

while input1!=0:
    print(input1)
    input1-=1

# Task 2 - Multiplication Table with for Loops
# Write a program that generates the multiplication table for any number provided by the user.

# Ask the user to input a number.
# Use a for loop to print the multiplication table for that number (from 1 to 10).
# Example Output:

# Enter a number: 4
# 4 x 1 = 4 4 x 2 = 8 ... 4 x 10 = 40

input2 = int(input("Enter a number "))

i = 1
while i!=11:
    print(f"{i}*{input2} is {i*input2}")
    i+=1

#Task 3 - Find the Factorial
# Write a Python program to calculate the factorial of a number entered by the user.

# Ask the user for a number.
# Use a for loop to calculate the factorial.
# Print the result in a friendly format.
# For example:

# Enter a number: 5
# The factorial of 5 is 120.
    
input3 = int(input("Enter a number "))
n = input3


total_product = 1

while n!=0:
    total_product*=n
    n-=1

print(f"Factorial of {input3} is {total_product}")


