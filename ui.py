def show_menu():
    print("\n1. calculate")
    print("2. view history")
    print("3. exit")

def show_operation_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

def format_record(record):
    return f"{record['num1']} {record['operator']} {record['num2']} = {record['result']}"

def show_history(history):
    if not history:
        print("No calculations yet.")
    else:
        print("\nCalculation History:")
        for record in history:
            print(format_record(record))

def get_user_input():
    while True:
        try:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")