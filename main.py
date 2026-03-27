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

def show_menu():
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def format_record(num1, num2, operator, result):
    return f"{num1} {operator} {num2} = {result}"

def show_history(history):
    if not history:
        print("No calculations yet.")
    else:
        print("\nCalculation History:")
        for record in history:
            print(format_record(*record))

def get_user_input():
    while True:
        try:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def calculate(num1, num2, choice):
    if choice == '1':
                result = add(num1, num2)
                operator = '+'
    elif choice == '2':
                result = subtract(num1, num2)
                operator = '-'
    elif choice == '3':
                result = multiply(num1, num2)
                operator = '*'
    elif choice == '4':
                result = divide(num1, num2)
                operator = '/'
    return result, operator

def ask_yes_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ['yes', 'y']:
            return True
        elif answer in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    print("Welcome to the Calculator CLI!")
    history = []
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == '5':
            break
        elif choice in ['1', '2', '3', '4']:
            print("You chose option", choice)
            num1, num2 = get_user_input()
            result, operator = calculate(num1, num2, choice)
            print(format_record(num1, num2, operator, result))
            history.append((num1, num2, operator, result))
            print()
            if ask_yes_no("\nview history? (yes/no): "):
                show_history(history)
            if not ask_yes_no("\nWould you like to perform another operation? (yes/no): "):
                break
        else:
            print("Invalid choice. Please select a valid operation.")
    print("Thank you for using the Calculator CLI. Goodbye!")
        
if __name__ == "__main__":
    main()