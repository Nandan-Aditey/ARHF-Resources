# P9 
 
def first_vowel(s: str) -> str:
    """Find the first vowel in s.
    >>> first_vowel('apple')
        'a'
    """
    
    # Specification Detail 1: What if there are no vowels?
    # Desired Interpretation: If there are no vowels, return '-'
    
    # Specification Detail 2: If lower case assumed, in alphabetical or index, which order?
    # Desired Interpretation: Return the first vowel present in alphabetical order (a->e->i->o->u)
    
    # Specification Detail 3: Return in alphabetical, ASCII, index, which order, and to preserve case or not
    # Desired Interpretation: Alphabetical and don't preserve case - lowercase
    
    # Specification Detail 2 and 3 might seem like a mixture of ambiguities, however you won't have different ordering with ASCII if lowercase was assumed 
    
 
    s = s.lower()
    for v in 'aeiou':
        if v in s:
            return v
    return '-'
    