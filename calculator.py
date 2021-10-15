def calculator(number1, number2, operator):
    """
    User inputs an equation in the format of:
    A + B
    If ZeroDivision Error occurs returns False

    Parameter
    ---------
    number1

    number2

    operator

    """
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
            return number1 * number2
    elif operator == "/":
        #If number2 is equal to 0 returns false due to ZeroDivisionError
        if number2 == 0:
            return (False)
        else:
            return number1 / number2
    elif operator == "//":
        #If number2 is equal to 0 returns false due to ZeroDivisionError
        if number2 == 0:
            return (False)
        else:
            return number1 // number2  
    elif operator == "**":
        return number1 ** number2
    else:
        return (False)
                
def parse_input():
    """
    Takes user input and splits the input into: 
    first_number, operator, second_number
    Calls calculator function in the print statement, and prints result.
    """
    equation = input("Enter equation: ")
    # Use equation.split to create a list of strings
    first_number, operator, second_number = equation.split()
    first_number = float(first_number)
    second_number = float(second_number)
    print(calculator(first_number,second_number,operator))

parse_input()