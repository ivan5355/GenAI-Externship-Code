# Task 1 - String Slicing and Indexing

# Create a string variable with the value "Python is amazing!".
# Extract the following using slicing:
# The first 6 characters ("Python")
# The word "amazing"
# The entire string in reverse order
# Print each of these slices with a clear label.
# Example Output:

# First word: Python
# Amazing part: amazing
# Reversed string: !gnizama si nohtyP

phrase = "Python is amazing!"

#Python
part1 = phrase[0:6]
print(part1)

#amazing
part2 = phrase[10:17]
print(part2)

#entire string in reverse order
part3 = phrase[::-1]
print(part3)

# Task 2 - String Methods

# Create a string with the value " hello, python world! ".
# Use the following string methods and print the results:
# strip() to remove extra spaces
# capitalize() to capitalize the first letter
# replace() to replace "world" with "universe"
# upper() to convert the string to uppercase

phrase_2 = " hello, python world! "

#remve extra phrases
stripped_phrase = phrase_2.strip()
print(stripped_phrase)

# capitalize() to capitalize the first letter
captalized = phrase_2.capitalize()
print(captalized)

# replace() to replace "world" with "universe"
replaced = phrase_2.replace("world","universe")
print(replaced)

# upper() to convert the string to uppercase
all_caps = phrase_2.upper()
print(all_caps)


# Task 3 - Check for Palindromes
# Write a Python program to check if a string is a palindrome (reads the same backward and forward).

# Ask the user to input a word.
# Use slicing to reverse the string and compare it with the original.
# Print a friendly message indicating whether the word is a palindrome.
# Example Run:

# Enter a word: madam
# Yes, 'madam' is a palindrome!
user_input = input("Enter a word ")
backwards_user_input = user_input[::-1]
print(backwards_user_input)

if user_input == backwards_user_input:
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} is not a palindrome!")



