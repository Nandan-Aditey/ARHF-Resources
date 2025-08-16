def num_digits_I1(n: int) -> int:
    """Count the number of digits in n.
    >>> num_digits(123)
        3
    """
    
    # Interpretation-1 (C1)
    # Count all the digits in n.

    return len(str(abs(n)))
 
 
def num_digits_I2(n: int) -> int:
    """Count the number of digits in n.
    >>> num_digits(123)
        3
    """
 
    # Interpretation-2 (C2)
    # Count the uniqiue digits in n.

    return len(set(str(abs(n))))