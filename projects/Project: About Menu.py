import turtle

# Step 2: Recursive Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Step 3: Recursive Fibonacci Function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Step 4: Recursive Fractal Tree Pattern (Bonus)
def draw_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15, t)
        t.left(40)
        draw_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

# Helper: Validate positive integer input
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

# Step 1 & 5: Main Menu
def main():
    print("🌟 Welcome to the Recursive Artistry Program! 🌟")

    while True:
        print("\nChoose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci Number")
        print("3. Draw Recursive Fractal Tree (Bonus)")
        print("4. Exit")

        choice = input("> ")

        if choice == '1':
            n = get_positive_int("Enter a number to find its factorial: ")
            print(f"The factorial of {n} is {factorial(n)}.")

        elif choice == '2':
            n = get_positive_int("Enter the position of the Fibonacci number: ")
            print(f"The {n}th Fibonacci number is {fibonacci(n)}.")

        elif choice == '3':
            print("Drawing a recursive fractal tree...")
            screen = turtle.Screen()
            t = turtle.Turtle()
            t.left(90)
            t.speed(0)
            draw_tree(100, t)
            screen.exitonclick()

        elif choice == '4':
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

# Run the program
if __name__ == "__main__":
    main()
