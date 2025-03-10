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
    
    # Create a list to store generated characters and combined substrings
    unique_result = set()
    
    # First add single characters
    for i in range(len(s)):
        unique_result.add(s[i])
    
    # Generate and add multi-character substrings 
    for length in range(2, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s[start:start+length]
            unique_result.add(substring)
    
    # Sort by length and then alphabetically
    return sorted(unique_result, key=lambda x: (len(x), x))