

# ===== TASK 1: Understanding Python Exceptions =====
def task1_divide_hundred():

    """Task 1: Function to divide 100 by user input with proper exception handling."""
    print("=== Task 1: Understanding Python Exceptions ===")
    print("This task demonstrates handling ZeroDivisionError and ValueError")
    print()
    
    while True:
        try:
            # Prompt user for input
            user_input = input("Enter a number: ")
        
            # Convert to float (this can raise ValueError)
            number = float(user_input)
            
            # Perform division (this can raise ZeroDivisionError)
            result = 100 / number
            
            # If no exceptions occurred, print result and break
            print(f"100 divided by {number} is {result}")
            break
            
        except ZeroDivisionError:

            # Handle division by zero
            print("Oops! You cannot divide by zero.")
            
        except ValueError:
            # Handle non-numeric input
            print("Invalid input! Please enter a valid number.")

# ===== TASK 2: Types of Exceptions =====
def task2_demonstrate_index_error():
    """Demonstrate IndexError by accessing invalid list index."""
    try:
        # Create a list with 3 elements (indices 0, 1, 2)
        my_list = [1, 2, 3]
        
        # This will raise an IndexError because the list only has indices 0-2
        value = my_list[5]
        print(f"Value at index 5: {value}")
        
    except IndexError:
        # Handle the IndexError when trying to access an invalid index
        print("IndexError occurred! List index out of range.")

def task2_demonstrate_key_error():
    """Demonstrate KeyError by accessing non-existent dictionary key."""
    try:
        # Create a dictionary with specific keys
        my_dict = {"name": "Alice", "age": 25, "city": "New York"}
        

        # This will raise a KeyError because "country" is not a key in the dictionary
        value = my_dict["country"]
        print(f"Country: {value}")
        
    except KeyError:
        # Handle the KeyError when trying to access a non-existent key
        print("KeyError occurred! Key not found in the dictionary.")

def task2_demonstrate_type_error():
    """Demonstrate TypeError by adding incompatible types."""
    try:
    
        # This will raise a TypeError because Python cannot directly add these different types
        result = "Hello" + 42
        print(f"Result: {result}")
        
    except TypeError:
        # Handle the TypeError when trying to perform invalid operations between types
        print("TypeError occurred! Unsupported operand types.")

def task2_demonstrate_all_exceptions():
    """Run all exception demonstrations for Task 2."""
    print("=== Task 2: Types of Exceptions ===")
    print("This task demonstrates IndexError, KeyError, and TypeError")
    print()
    
    print("1. Demonstrating IndexError:")
    task2_demonstrate_index_error()
    print()
    
    print("2. Demonstrating KeyError:")
    task2_demonstrate_key_error()
    print()
    
    print("3. Demonstrating TypeError:")
    task2_demonstrate_type_error()
    print()

# ===== TASK 3: Using try...except...else...finally =====
def task3_divide_two_numbers():
    """Task 3: Function to divide two user-entered numbers using try/except/else/finally."""
    try:
        
        # try block: attempt to get input and perform division
        print("=== Task 3: Using try...except...else...finally ===")
        print("This task demonstrates the complete try/except/else/finally structure")
        print()
        
        # Get first number from user
        first_input = input("Enter the first number: ")
        first_number = float(first_input)
        
        # Get second number from user
        second_input = input("Enter the second number: ")
        second_number = float(second_input)
        
        # Attempt division (this could raise ZeroDivisionError)
        result = first_number / second_number
        
    except ValueError:
        # except block: handle invalid input (non-numeric values)
        print("Error: Invalid input! Please enter valid numbers.")
        
    except ZeroDivisionError:
        # except block: handle division by zero
        print("Error: Cannot divide by zero!")
        
    except Exception as e:
        # except block: handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        
    else:
        # else block: executes only if no exceptions occurred in the try block
        print(f"The result is {result}")
        
    finally:
        # finally block: always executes regardless of whether exceptions occurred
        print("This block always executes.")

# ===== MAIN PROGRAM =====
def display_menu():
    """Display the main menu for task selection."""
    print("\n" + "="*60)
    print("Python Exception Handling - Assignment Menu")
    print("="*60)
    print("1. Task 1: Understanding Python Exceptions")
    print("2. Task 2: Types of Exceptions")
    print("3. Task 3: Using try...except...else...finally")
    print("4. Run All Tasks")
    print("5. Exit")
    print("="*60)

def run_all_tasks():
    """Run all three tasks sequentially."""
    print("\n" + "="*60)
    print("Running All Tasks Sequentially")
    print("="*60)
    
    # Task 1
    task1_divide_hundred()
    print("\n" + "-"*40 + "\n")
    
    # Task 2
    task2_demonstrate_all_exceptions()
    print("-"*40 + "\n")
    
    # Task 3
    task3_divide_two_numbers()

def main():
    """Main function to run the exception handling assignment."""
    print("Welcome to the Python Exception Handling Assignment!")
    print("This program demonstrates various exception handling concepts.")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                print()
                task1_divide_hundred()
                
            elif choice == "2":
                print()
                task2_demonstrate_all_exceptions()
                
            elif choice == "3":
                print()
                task3_divide_two_numbers()
                
            elif choice == "4":
                run_all_tasks()
                
            elif choice == "5":
                print("\nThank you for exploring Python exception handling!")
                print("Remember: Proper exception handling makes your code more robust and user-friendly.")
                break
                
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Ask if user wants to continue
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main() 