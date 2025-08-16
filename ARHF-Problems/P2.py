def min_freq_I1(data: list[int]) -> int | None:
    """Find the minimum frequency. Return None if data is empty.
    >>> min_freq([1, 2, 1])
        2
    """
    
    # Interpretation-1 (C1)
    # Find the minimum number in the list and find its frequency

    if not data: 
        return None
    return data.count(min(data))
 
 
def min_freq_I2(data: list[int]) -> int | None:
    """Find the minimum frequency. Return None if data is empty.
    >>> min_freq([1, 2, 1])
        2
    """

    # Interpretation-2 (C2)
    # Find the smallest number which has the minimum frequency

    if not data: 
        return None
    temp = {x: data.count(x) for x in set(data)}
    c = min(temp.values())
    return min(x for x, y in temp.items() if y == c)
 
 
def min_freq_I3(data: list[int]) -> int | None:
    """Find the minimum frequency. Return None if data is empty.
    >>> min_freq([1, 2, 1])
        2
    """
    # Interpretation-3 (C3)
    # Find the largest number which has the maximum frequency

    if not data: 
        return None
    temp = {x: data.count(x) for x in set(data)}
    c = min(temp.values())
    return max(x for x, y in temp.items() if y == c)