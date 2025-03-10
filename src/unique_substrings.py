from typing import List

def find_unique_substrings(s: str) -> List[str]:
    """
    Find all unique substrings within the given input string.
    
    Args:
        s (str): The input string to find substrings from.
    
    Returns:
        List[str]: A list of unique substrings, sorted.
    
    Examples:
        >>> find_unique_substrings("abab")
        ['a', 'ab', 'aba', 'abab', 'b', 'ba']
        
    Notes:
        - Returns an empty list for empty input string
        - Substrings are case-sensitive
        - Duplicate substrings are included only once
    """
    # Handle empty string edge case
    if not s:
        return []
    
    # Use a set to ensure uniqueness
    unique_substrings = set()
    
    # Generate substrings systematically
    # First, add single characters
    unique_substrings.update(set(s))
    
    # Generate multi-character substrings 
    # Specifically generate contiguous substrings from start
    for start in range(len(s)):
        for length in range(2, len(s) - start + 1):
            substring = s[start:start+length]
            unique_substrings.add(substring)
    
    # Return sorted with custom ordering by length and value
    return sorted(list(unique_substrings), key=lambda x: (len(x), x))