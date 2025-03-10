from typing import List

def find_unique_substrings(s: str) -> List[str]:
    """
    Find all unique substrings within the given input string.
    
    Args:
        s (str): The input string to find substrings from.
    
    Returns:
        List[str]: A list of unique substrings, sorted alphabetically.
    
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
    
    # Use a set to ensure uniqueness, then convert to sorted list
    unique_substrings = set()
    
    # Generate all possible substrings systematically
    for length in range(1, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start+length]
            unique_substrings.add(substring)
    
    # Return sorted list of unique substrings
    return sorted(list(unique_substrings))