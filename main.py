def add(n1, n2):
    """Returns the sum of 2 numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Returns the subtraction result of 2 numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Returns the muliplication result of 2 numbers"""
    return n1 * n2

def divide(n1, n2):
    """Returns the division result of 2 numbers"""
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input('Pick an operation from the line above: ')
num2 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')