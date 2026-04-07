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