# P7

def count_between(data: list[int], a: int, b: int) -> int:
    """Count the number of integers in data between a and b.
    >>> count_between([1, 2, 3], 0, 5)
        3
    """
    
    # Specification Detail 1: Count total number or only the unique numbers
    # Desired Interpretation: Count the total number, not unique
    
    # Specification Detail 2: What if a > b, swap a and b or return 0?
    # Desired Interpretation: If a > b, swap the two
    
    # Specification Detail 3: Include endpoint a or not?
    # Desired Interpretation: Have strict inequality at endpoint a
    
    # Specification Detail 4: Include endpoint b or not?
    # Desired Interpretation: Have strict inequality at endpoint b

    
    if a > b:
        a, b = b, a
    return sum(1 for x in data if a < x < b)