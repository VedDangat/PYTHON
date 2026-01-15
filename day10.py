'''def formated_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
print(formated_name("ved", "dangat"))


def function_1(text):
    return text+text

def function_2(text):
    return text.title()

op=function_2(function_1("hello"))
print(op)

def is_leap_year(year):
    """
    Determines whether a given year is a leap year.

    A leap year is:
    - Divisible by 4
    - Not divisible by 100 unless also divisible by 400

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2020))
print(is_leap_year(1990))
from random import choice

print("""
 ┌──────────────────┐  
 │   Pythonista  0. │
 ├──────────────────┤
 │ 7 │ 8 │ 9 │  +  │
 ├───┼───┼───┼─────┤
 │ 4 │ 5 │ 6 │  -  │
 ├───┼───┼───┼─────┤
 │ 1 │ 2 │ 3 │  x  │
 ├───┼───┼───┼─────┤
 │ 0 │ . │ = │  /  │
 └──────────────────┘


 ██████╗   █████╗  ██╗      ██████╗
██╔════╝  ██╔══██╗ ██║     ██╔════╝
██║       ███████║ ██║     ██║     
██║       ██╔══██║ ██║     ██║     
╚██████╗  ██║  ██║ ███████╗╚██████╗
 ╚═════╝  ╚═╝  ╚═╝ ╚══════╝ ╚═════╝
""")

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
    "/": divide
}

should_accumulate = True
num1 = float(input("Enter first number: "))

while should_accumulate:

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Enter operation to perform: ")
    num2 = float(input("Enter second number: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"The result: {num1} {operation_symbol} {num2} = {answer}")

    choice = input(
        f"Type 'yes' to continue calculating with {answer}, or type 'no' to start a new calculation: "
    ).lower()

    if choice == "yes":
        num1 = answer
    else:
        should_accumulate = False
        print("Calculator stopped.")'''


