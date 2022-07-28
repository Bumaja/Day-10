from art import logo
from os import system

def calculation(a, b):
    if operation == "+":
        return a + b 
    elif operation == "-":
        return a - b 
    elif operation == "*":
        return a * b 
    elif operation == "/":
        return a / b 

def checker_first():
    number = input("What's the first number?: ")
    while number.isnumeric() == False:
        number = input("What's first number?: ")
    return int(number)
    
def checker_second():
    number = input("What's the second number?: ")
    while number.isnumeric() == False:
        number = input("What's first number?: ")
    return int(number)
        
clear = lambda: system("clear")
flag = True
op = ['+', '-', '*', '/']

while flag:
    print(logo)
    
    first_number = checker_first()
    second_number = checker_second()
    print("""+
-
*
/
    """)
    operation = input("Pick an operator from the listed above. ")
    
    if operation in op:
        result = calculation(first_number, second_number)
    else:
        print("You haven't chosen an operator. Choose one from listed: + - * /")
        continue
    print(f"{float(first_number)} {operation} {float(second_number)} = {float(result)}")
    cont = input(f"Type 'y' to continue calculating with {result}, otherwise type 'n' to start new calculating.\n")
    if cont == 'n':
        clear()
        continue
    elif cont == 'y':
        while flag == True:
            first_number = result
            operation = input("Pick an operator. ")
            second_number = int(input("What's the next number?: "))
            result = calculation(first_number, second_number)
            print(f"{float(first_number)} {operation} {float(second_number)} = {float(result)}")
            cont = input(f"Type 'y' to continue calculating with {result}, otherwise type 'n' to start new calculating.\n")
            if cont == 'n':
                clear()
                break
            elif cont == 'y':
                continue
        