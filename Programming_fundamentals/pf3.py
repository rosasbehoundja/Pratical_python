# a simple calculator for basic arithmetic operations

def introduction():
    choices = """
            Welcome to Mental! An awesome calculator for basic arithmetic operations.
        Check the operations list and choose one please. Just enter the number!
        1 - Addition
        2 - Soustraction
        3 - Multiplication
        4 - Division
"""
    return choices

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():

    print(introduction())

    while True:
        choice = input("Enter operation number (1-4) or 'q' to quit: ")
        
        if choice == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please try again.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")

        print()  # Print a blank line for readability

# Run the calculator
calculator()