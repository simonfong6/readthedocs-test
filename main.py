def sum(num1,num2):
    """
    Sums two numbers.

    Args:
        num1: First number to be added. Needs to be a numerical value.
        num2: Second number to be added. Needs to be a numerical value.
         
    Returns:
        int: Sum of the two numbers.

    Raises:
        TypeError: When it is not an int or float.
    
    """
    print("Hello World!!!")
    
    if(not isinstance(int)):
        raise TypeError("Is not an int.")

    return num1 + num2


if (__name__ == '__main__'):
    print("Hello World!!")
