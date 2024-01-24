# Calculator

from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator(): 
    print(logo)
    
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    keep_calculating = True

    while keep_calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}") 
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if should_continue == "y":
            num1 = answer
        else: 
            keep_calculating == False
            calculator()

calculator()
