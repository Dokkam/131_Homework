import time

def calculate_time(method):
    """
    Function takes the time at the start of the program,
    and subtracts it from the time the program finishes.

    Parameters
    ----------
    method: Any
    """
    def timer():
        startTime = time.time()
        method()
        print(f"Total time", (time.time() - startTime))

    return timer
