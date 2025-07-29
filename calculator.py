def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None, "Error! Division by zero."
    return a / b, None

def get_number(prompt):
    """Safely get a number from user input with error handling"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_choice():
    """Safely get menu choice from user with validation"""
    valid_choices = ['1', '2', '3', '4']
    while True:
        choice = input("Enter choice (1/2/3/4): ").strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice! Please enter 1, 2, 3, or 4.")

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = get_choice()

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    result, error = divide(num1, num2)
    if error:
        print(error)
    else:
        print("Result:", result)
