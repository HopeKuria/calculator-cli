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
history = []
while True:
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("\nEnter your choice (1-5): ")
    if choice in ['1', '2', '3', '4']:
        print("You chose option", choice)
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        if choice == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is {result}")
            history.append((num1, num2, '+', result))
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is {result}")
            history.append((num1, num2, '-', result))
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is {result}")
            history.append((num1, num2, '*', result))
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is {result}")
            history.append((num1, num2, '/', result))
        print()
        print("\nView history of calculations? (yes/no): ")
        view_history = input().lower()
        if view_history == 'yes' or view_history == 'y':
            for record in history:
                print(f"{record[0]} {record[2]} {record[1]} = {record[3]}")
        print("\nWould you like to perform another operation? (yes/no): ")
        another = input().lower()
        if another != 'yes' and another != 'y':
            break
    else:
        if choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid operation.")
print("Thank you for using the Calculator CLI. Goodbye!")