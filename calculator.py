def calculator(number1, number2, operator):
    """
    Checks user input for the correct operator.
    If the operator is invalid returns flase.
    If ZeroDivision Error occurs returns False

    Parameter
    ---------
    number1: float
        First user float input
    number2: float
        Second user float input
    operator: arithemetic operator
        User input for arithmetic operator

    Return
    ------
    False: str
        If operator is invalid, or if a ZeroDivisionError occurs
    number1 + number2: float
        Result of addition
    number1 - number2: float
        Result of subtraction
    number1 * number2: float
        Result of multiplication
    number1 / number2: float
        Result of division
    number1 // number2: float
        Result of floor division
    number1 ** number2: float
        Result of exponentation
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
    User inputs an equation in the format of:
    A + B
    Takes user input and splits the input into a list: 
    first_number, operator, second_number
    Calls calculator function in the print statement, and prints result.
    """
    equation = input("Enter equation: ")
    # Use equation.split to create a list of strings
    first_number, operator, second_number = equation.split()
    first_number = float(first_number)
    second_number = float(second_number)
    print(calculator(first_number,second_number,operator))

