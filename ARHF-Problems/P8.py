# P8
 
def smallest_even(data: list[int]) -> list[int]:
    """Search data for the smallest even value.
    >>> smallest_even([50, 25, 2, 30, 45])
        [2]
    """
    
    # Specification Detail 1: If there is no even, what to return? 
    # Desired Interpretation: If there are no even numbers, return the empty list []
    
    # Specification Detail 2: Exactly one smallest even or multiple?
    # Desired Interpretation: Multiple can be present
    
    # Specification Detail 3: If exactly one, return index or number?
    # Desired Interpretation: Return index
    
    # Specification Detail 4: If multiple, return index (all ascending, descending, first, last)
    # Desired Interpretation: Return the indices in descending order

    try:
        min_even = min(x for x in data if x % 2 == 0)
        return list(reversed([i for i, x in enumerate(data) if x == min_even]))
    except:
        return []