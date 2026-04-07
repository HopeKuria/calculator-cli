from calculator import calculate
from storage import load_history, save_history 
from ui import show_menu, show_operation_menu, get_user_input, format_record, show_history

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
                save_history(history)
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