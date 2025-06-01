"""
Personal Finance Tracker
A command-line application for tracking personal expenses with categorization and summary features.
"""

def print_welcome():
    """Print welcome message when the program starts."""
    print("Welcome to the Personal Finance Tracker!")
    print("=" * 40)

def add_expense(expenses_data):
    """
    Add a new expense to the data structure.
    
    Args:
        expenses_data (dict): Dictionary containing expense data
    """
    try:
        # Get expense description
        while True:
            description = input("Enter expense description: ").strip()
            if description:
                break
            print("Description cannot be empty. Please try again.")
        
        # Get category
        while True:
            category = input("Enter category: ").strip()
            if category:
                break
            print("Category cannot be empty. Please try again.")
        
        # Get amount with exception handling
        while True:
            try:
                amount_input = input("Enter amount: ").strip()
                if not amount_input:
                    print("Amount cannot be empty. Please try again.")
                    continue
                
                amount = float(amount_input)
                if amount < 0:
                    print("Amount cannot be negative. Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        # Store expense as tuple (description, amount)
        expense_tuple = (description, amount)
        
        # Add to dictionary - if category doesn't exist, create it
        if category not in expenses_data:
            expenses_data[category] = []
        
        expenses_data[category].append(expense_tuple)
        print("Expense added successfully.")
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_expenses(data):
    """
    Display all expenses organized by category.
    
    Args:
        data (dict): Dictionary containing expense data
    """
    if not data:
        print("No expenses recorded yet.")
        return
    
    print("\n--- All Expenses ---")
    for category, expenses in data.items():
        print(f"Category: {category}")
        for description, amount in expenses:
            print(f"  - {description}: ${amount:.2f}")
        print()  # Empty line for better readability

def view_summary(data):
    """
    Display summary of total expenses by category.
    
    Args:
        data (dict): Dictionary containing expense data
    """
    if not data:
        print("No expenses recorded yet.")
        return
    
    print("\n--- Summary ---")
    total_overall = 0
    
    for category, expenses in data.items():
        category_total = sum(amount for _, amount in expenses)
        print(f"{category}: ${category_total:.2f}")
        total_overall += category_total
    
    print("-" * 20)
    print(f"Total: ${total_overall:.2f}")

def display_menu():
    """Display the main menu options."""
    print("\nWhat would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")

def get_menu_choice():
    """
    Get user's menu choice with input validation.
    
    Returns:
        int: User's menu choice (1-4)
    """
    while True:
        try:
            choice = input("Choose an option: ").strip()
            if not choice:
                print("Please enter a choice.")
                continue
            
            choice_num = int(choice)
            if 1 <= choice_num <= 4:
                return choice_num
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return 4  # Exit option

def main():
    """Main function that controls the program flow."""
    # Initialize data structure - dictionary with category as key, list of tuples as values
    expenses_data = {}
    
    # Print welcome message
    print_welcome()
    
    # Main program loop
    while True:
        try:
            display_menu()
            choice = get_menu_choice()
            
            if choice == 1:
                print("\n--- Add Expense ---")
                add_expense(expenses_data)
            
            elif choice == 2:
                view_expenses(expenses_data)
            
            elif choice == 3:
                view_summary(expenses_data)
            
            elif choice == 4:
                print("Goodbye!")
                break
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
