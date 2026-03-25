print("Welcome to the Calculator CLI!")
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
while True:
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice in ['1', '2', '3']:
        print("You chose option", choice)
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        if choice == '1':
            print(f"The result of {num1} + {num2} is {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of {num1} * {num2} is {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result of {num1} / {num2} is {divide(num1, num2)}")
    else:
        if choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid operation.")
print