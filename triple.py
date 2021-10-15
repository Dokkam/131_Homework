def tripler(method):
    """
    
    """
    def decorator():
        for line in range(3):
            method()
    return decorator

@tripler
def threeTimes():
    """

    """
    string = "Test"
    print (string)

threeTimes()