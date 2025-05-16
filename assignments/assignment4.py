# Create a list of your favorite fruits. Add at least five fruits to the list.
# Perform the following operations:
# Append a new fruit to the list.
# Remove one fruit from the list using the remove() method.
# Print the list in reverse order using slicing.
# Example Output:

# Original list: ['apple', 'banana', 'cherry', 'date', 'elderberry']
# After adding a fruit: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
# After removing a fruit: ['banana', 'cherry', 'date', 'elderberry', 'fig']
# Reversed list: ['fig', 'elderberry', 'date', 'cherry', 'banana']

original_list =  ['apple', 'banana', 'cherry', 'date', 'elderberry']

#append
original_list.append("pineapple")
print(original_list)

#remove
original_list.remove("cherry")
print(original_list)

#revrse
print(original_list[::-1])

# Task 2 - Exploring Dictionaries

# Create a dictionary to store information about yourself with the following keys: "name", "age", "city".
# Add a new key-value pair to the dictionary for "favorite color".
# Update the "city" key with a new value.
# Print all the keys and values using a loop.
# Example Output:

# Keys: name, age, city, favorite color
# Values: Alice, 25, New York, Blue

about_me = {"name":"Ivan", "age":23, "city": "New York"}
about_me["favorite_color"] = "blue"

for key, value in about_me.items():
    print(key,value)

# Task 3 - Using Tuples

# Create a tuple with three elements: your favorite movie, song, and book.
# Try to change one of the elements (you’ll see why tuples are immutable!).
# Print the length of the tuple using the len() function.
# Example Output:

# Favorite things: ('Inception', 'Bohemian Rhapsody', '1984')
# Oops! Tuples cannot be changed.
# Length of tuple: 3
    
favorite_things = ("Interstellar", "Rocket Man", "Harry Potter")
print(len(favorite_things))