def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


print(logo)
keep_going = 'y'
first_time = True

while True:
    if first_time == True:
        first_number = float(input("What's the first number?:  "))

    print(
        "+\n"
        "-\n"
        "*\n"
        "/\n"
    )
    op = input("Pick an operation: ")
    next_number = float(input("What's the next number?:  "))

    if op == "+":
        result = operations["+"](first_number, next_number)
    elif op == "-":
        result = operations["-"](first_number, next_number)
    elif op == "*":
        result = operations["*"](first_number, next_number)
    elif op == "/":
        result = operations["/"](first_number, next_number)
    else:
        print("You entered an incorrect operation. Try again.")
        continue

    print(f"{first_number} {op} {next_number} = {result}")

    keep_going = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if keep_going == 'y':
        first_time = False
        first_number = result
    else:
        first_time = True

