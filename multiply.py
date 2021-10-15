def multiply_list(myList):
    """
    Function takes list.
    Then multiplies each element and reuturns result.
    If there's an error returns false.

    Parameters
    ----------
    myList: Any
        
    """
    result = 1
    for x in myList:
        if (isinstance(x, int)):
            result = result * x
        else:
            return False
    return result;

input1 = [1, 2, 3, 7]
input2 = [3, 2, 4, 89]
print (multiply_list(input1))
print(multiply_list(input2))

