import json

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
    print("\n1. calculate")
    print("2. view history")
    print("3. exit")

def show_operation_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

def save_to_file(history):
    with open("history.json", "w") as file:
        json.dump(history, file, indent=4)

def format_record(record):
    return f"{record['num1']} {record['operator']} {record['num2']} = {record['result']}"

def show_history(history):
    if not history:
        print("No calculations yet.")
    else:
        print("\nCalculation History:")
        for record in history:
            print(format_record(record))

def load_history():
    try:
        with open("history.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def get_user_input():
    while True:
        try:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def calculate(num1, num2, choice):
    operations = {
        '1': (add, '+'),
        '2': (subtract, '-'),
        '3': (multiply, '*'),
        '4': (divide, '/')
    }
    func, operator = operations[choice]
    result = func(num1, num2)
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
    history = load_history()
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-3): ")
        if choice == '1':
            show_operation_menu()
            operation_choice = input("\nSelect an operation (1-4): ")
            if operation_choice in ['1', '2', '3', '4']:
                num1, num2 = get_user_input()
                result, operator = calculate(num1, num2, operation_choice)
                record = {
                    'num1': num1,
                    'num2': num2,
                    'operator': operator,
                    'result': result
                }
                print(format_record(record))
                history.append(record)
                save_to_file(history)
                print()
            else:
                print("Invalid operation choice. Please select a valid operation.")
        elif choice == '2':
            show_history(history)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select a valid option.")
    print("Thank you for using the Calculator CLI. Goodbye!")
        
if __name__ == "__main__":
    main()