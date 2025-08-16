def min_index_I1(s: str) -> int:
    """Find the index of the smallest digit ('0' to '9') in s.
    >>> min_index('2025')
        1
    """
    
    # Interpretation-1 (C1)
    # Return the first index of the smallest digit
    # Return -1 if there is no digit
    
    for d in '0123456789':
        result = s.find(d)
        if result >= 0: 
            return result
    return -1
 

def min_index_I2(s: str) -> int:
    """Find the index of the smallest digit ('0' to '9') in s.
    >>> min_index('2025')
        1
    """
 
    # Interpretation-2 (C2)
    # Return the first index of the smallest digit
    # Return len(s) if there is no digit
    
    for d in '0123456789':
        result = s.find(d)
        if result >= 0: 
            return result
    return len(s)
 

def min_index_I3(s: str) -> int:
    """Find the index of the smallest digit ('0' to '9') in s.
    >>> min_index('2025')
        1
    """
 
    # Interpretation-3 (C3)
    # Return the last index of the smallest digit
    # Return -1 if there is no digit
    
    for d in '0123456789':
        result = s.rfind(d)
        if result >= 0: 
            return result
    return -1
 
 
def min_index_I4(s: str) -> int:
    """Find the index of the smallest digit ('0' to '9') in s.
    >>> min_index('2025')
        1
    """

    # Interpretation-4 (C4)
    # Return the last index of the smallest digit
    # Return len(s) if there is no digit
    
    for d in '0123456789':
        result = s.rfind(d)
        if result >= 0: 
            return result
    return len(s)