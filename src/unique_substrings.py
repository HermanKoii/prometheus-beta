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
    
    # Carefully generate substrings
    for start in range(len(s)):
        # Add single characters
        unique_substrings.add(s[start])
        
        # Add all consecutive substrings starting from this position
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            # Only add the substring if it's different lengths
            unique_substrings.add(substring)
    
    # Custom sorting that prioritizes length and alphabetic order
    return sorted(list(unique_substrings), key=lambda x: (len(x), x))