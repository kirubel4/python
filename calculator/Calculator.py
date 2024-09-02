from art import logo
from os import system
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multi(a, b):
    return a * b
def divide(a, b):
    return a / b
operation = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    for i in operation:
        print(i)
        pack = True
    while pack:
        symbole = input("Choose operation sign from above: ")
        num2 = float(input("Enter the next number: "))
        function_operation = operation[symbole]
        answer = function_operation(num1, num2)
        print(f"{num1} {symbole} {num2} = {answer}")
        ask = input(f"Do you want to continue with the current value, 'y' to continue : 'n' to start again: press any key to quit: ")
        if ask == 'y':
            num1 = answer
        elif ask == 'n':
            system('cls')
            calculator()
        else:
            break 
calculator()