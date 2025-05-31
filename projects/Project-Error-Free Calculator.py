import logging
import os
from datetime import datetime

# ===== LOGGING SETUP =====
def setup_logging():
    """Set up logging configuration to log errors to error_log.txt"""
    logging.basicConfig(
        filename='error_log.txt',
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

# ===== INPUT VALIDATION FUNCTIONS =====
def get_valid_number(prompt):
    """
    Get a valid number from user input with proper exception handling.
    
    Args:
        prompt (str): The prompt message to display to the user
        
    Returns:
        float: A valid number entered by the user
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            # Check for empty input
            if not user_input:
                print("Error: Please enter a value, don't leave it empty.")
                continue
                
            # Try to convert to float
            number = float(user_input)
            return number
            
        except ValueError as e:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: {e} - User input: '{user_input}'")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            logging.error(f"Unexpected error in get_valid_number: {e}")

def get_menu_choice():
    """
    Get a valid menu choice from the user.
    
    Returns:
        str: Valid menu choice (1-5)
    """
    while True:
        try:
            choice = input("\n> ").strip()
            
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
                
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            logging.error(f"Unexpected error in get_menu_choice: {e}")

# ===== CALCULATOR OPERATIONS =====
def perform_addition(num1, num2):
    """Perform addition operation."""
    try:
        result = num1 + num2
        return result, True
    except Exception as e:
        logging.error(f"Error in addition: {e}")
        return None, False

def perform_subtraction(num1, num2):
    """Perform subtraction operation."""
    try:
        result = num1 - num2
        return result, True
    except Exception as e:
        logging.error(f"Error in subtraction: {e}")
        return None, False

def perform_multiplication(num1, num2):
    """Perform multiplication operation."""
    try:
        result = num1 * num2
        return result, True
    except Exception as e:
        logging.error(f"Error in multiplication: {e}")
        return None, False

def perform_division(num1, num2):
    """
    Perform division operation with specific exception handling.
    
    Args:
        num1 (float): Dividend
        num2 (float): Divisor
        
    Returns:
        tuple: (result, success_flag)
    """
    try:
        # Check for division by zero
        if num2 == 0:
            raise ZeroDivisionError("division by zero")
            
        result = num1 / num2
        return result, True
        
    except ZeroDivisionError as e:
        print("Oops! Division by zero is not allowed.")
        logging.error(f"ZeroDivisionError occurred: {e}")
        return None, False
        
    except Exception as e:
        print(f"An unexpected error occurred during division: {e}")
        logging.error(f"Unexpected error in division: {e}")
        return None, False

# ===== MENU AND INTERFACE FUNCTIONS =====
def display_menu():
    """Display the main calculator menu."""
    print("\n" + "="*50)
    print("🧮 Welcome to the Error-Free Calculator! 🧮")
    print("="*50)
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction") 
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("="*50)

def get_two_numbers():
    """
    Get two numbers from the user with validation.
    
    Returns:
        tuple: (num1, num2) or (None, None) if operation was cancelled
    """
    try:
        print("\nPlease enter two numbers for the calculation:")
        num1 = get_valid_number("Enter the first number: ")
        num2 = get_valid_number("Enter the second number: ")
        return num1, num2
    except KeyboardInterrupt:
        return None, None

def execute_operation(choice):
    """
    Execute the selected calculator operation.
    
    Args:
        choice (str): The menu choice selected by user
        
    Returns:
        bool: True if operation completed successfully, False otherwise
    """
    operation_map = {
        '1': ('Addition', perform_addition),
        '2': ('Subtraction', perform_subtraction),
        '3': ('Multiplication', perform_multiplication),
        '4': ('Division', perform_division)
    }
    
    if choice not in operation_map:
        return False
        
    operation_name, operation_func = operation_map[choice]
    
    try:
        # Get input numbers
        num1, num2 = get_two_numbers()
        
        # Check if operation was cancelled
        if num1 is None or num2 is None:
            print("Operation cancelled.")
            return True
            
        # Display operation being performed
        operator_symbols = {'1': '+', '2': '-', '3': '*', '4': '/'}
        symbol = operator_symbols[choice]
        
        print(f"\nPerforming: {num1} {symbol} {num2}")
        
        # Perform the calculation
        result, success = operation_func(num1, num2)
        
        if success:
            print(f"Result: {num1} {symbol} {num2} = {result}")
        else:
            print("Operation failed due to an error.")
            
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return True
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"Unexpected error in execute_operation: {e}")
        
    finally:
        # This block always executes
        print("Operation processing completed.")
        
    return True

# ===== MAIN PROGRAM =====
def main():
    """Main function to run the Error-Free Calculator."""
    # Setup logging
    setup_logging()
    
    # Log program start
    logging.info("Error-Free Calculator started")
    
    try:
        print("🎉 Welcome to the Error-Free Calculator!")
        print("This calculator handles errors gracefully and logs them for debugging.")
        
        while True:
            try:
                # Display menu and get user choice
                display_menu()
                choice = get_menu_choice()
                
                # Handle exit choice
                if choice == '5':
                    print("\n👋 Goodbye! Thank you for using the Error-Free Calculator!")
                    print("Remember: Proper exception handling makes software robust and user-friendly.")
                    break
                
                # Execute the selected operation
                success = execute_operation(choice)
                
                if not success:
                    print("Failed to execute operation. Please try again.")
                
                # Ask if user wants to continue
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user. Goodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred in main loop: {e}")
                logging.error(f"Unexpected error in main loop: {e}")
                
                # Ask if user wants to continue after error
                try:
                    continue_choice = input("Would you like to continue? (y/n): ").lower()
                    if continue_choice != 'y':
                        break
                except:
                    break
                    
    except Exception as e:
        print(f"A critical error occurred: {e}")
        logging.critical(f"Critical error in main: {e}")
        
    finally:
        # Log program end
        logging.info("Error-Free Calculator ended")
        print("\nProgram terminated.")
        
        # Show log file location if it exists
        if os.path.exists('error_log.txt'):
            print("📝 Error log has been saved to 'error_log.txt'")

if __name__ == "__main__":
    main() 