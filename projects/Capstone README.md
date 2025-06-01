# Personal Finance Tracker

A command-line Python application for tracking personal expenses with categorization and summary features. This project demonstrates core Python programming concepts including data structures, functions, exception handling, and user input validation.

## Project Overview

The Personal Finance Tracker allows users to:
- Add expenses with description, category, and amount
- View all recorded expenses organized by category
- View summary statistics showing total spending per category
- Handle invalid inputs gracefully with comprehensive error handling
- Navigate through a user-friendly menu-driven interface

## Features

- **Expense Management**: Add, view, and categorize expenses
- **Data Organization**: Uses dictionaries and tuples for efficient data storage
- **Input Validation**: Comprehensive error handling for user inputs
- **Summary Reports**: View spending totals by category and overall
- **User-Friendly Interface**: Clear menu system with intuitive navigation

## How to Run

1. **Prerequisites**: Ensure you have Python 3.x installed on your system

2. **Download the file**: Save the `capstone_project.py` file to your desired directory

3. **Run the application**:
   ```bash
   python capstone_project.py.py
   ```
   or
   ```bash
   python3 capstone_project.py.py
   ```

4. **Using the Application**:
   - Follow the on-screen prompts
   - Choose options 1-4 from the main menu
   - Enter expense details when prompted
   - View your expenses and summaries anytime

## Sample Usage

```
Welcome to the Personal Finance Tracker!
========================================

What would you like to do?
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit
Choose an option: 1

--- Add Expense ---
Enter expense description: Lunch
Enter category: Food
Enter amount: 12.5
Expense added successfully.

What would you like to do?
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit
Choose an option: 2

--- All Expenses ---
Category: Food
  - Lunch: $12.50

What would you like to do?
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit
Choose an option: 3

--- Summary ---
Food: $12.50
--------------------
Total: $12.50
```

## Python Concepts Demonstrated

### Core Programming Concepts
- **Variables and Data Types**: Strings, floats, integers
- **Control Structures**: if/elif/else statements, conditional logic
- **Loops**: while loops for menu navigation and input validation
- **Functions**: Modular code organization with dedicated functions for each feature

### Data Structures
- **Lists**: Storing multiple expenses within each category
- **Dictionaries**: Organizing expenses by category (key-value pairs)
- **Tuples**: Storing expense data as immutable (description, amount) pairs

### Advanced Features
- **Exception Handling**: try-except blocks for input validation and error management
- **String Operations**: Input processing, formatting, and validation
- **User Input/Output**: Interactive command-line interface
- **Code Organization**: Clean function structure and separation of concerns

### Specific Python Features Used
- **Dictionary Methods**: `.items()`, `.keys()`, membership testing
- **List Operations**: `.append()`, list comprehensions
- **String Methods**: `.strip()`, `.format()`, f-strings
- **Built-in Functions**: `input()`, `print()`, `float()`, `int()`, `sum()`
- **Error Handling**: `ValueError`, `KeyboardInterrupt`, generic exceptions

## Code Structure

The application is organized into several key functions:

- `main()`: Controls the overall program flow and menu system
- `add_expense()`: Handles expense input with validation
- `view_expenses()`: Displays all expenses organized by category
- `view_summary()`: Shows spending totals and summaries
- `display_menu()`: Shows the main menu options
- `get_menu_choice()`: Handles menu selection with validation
- `print_welcome()`: Displays the welcome message

## Error Handling

The application includes comprehensive error handling for:
- Non-numeric input for amounts
- Empty or whitespace-only inputs
- Negative amounts
- Invalid menu choices
- Keyboard interrupts (Ctrl+C)
- Unexpected errors

## Data Storage

Expenses are stored in a dictionary structure:
```python
{
    "Food": [("Lunch", 12.5), ("Coffee", 4.0)],
    "Transport": [("Bus fare", 2.5), ("Gas", 45.0)],
    "Entertainment": [("Movie", 15.0)]
}
```

This structure allows for efficient categorization and easy calculation of category totals.

## Future Enhancements

Potential improvements could include:
- Data persistence (saving to file)
- Date tracking for expenses
- Expense editing and deletion
- Budget tracking and alerts
- Data export functionality
- Graphical user interface 