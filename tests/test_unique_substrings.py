import pytest
from src.unique_substrings import find_unique_substrings

def test_find_unique_substrings_basic():
    """Test basic substring generation"""
    result = find_unique_substrings("abab")
    assert set(result) == {"a", "ab", "aba", "abab", "b", "ba"}

def test_find_unique_substrings_empty_string():
    """Test handling of empty string"""
    assert find_unique_substrings("") == []

def test_find_unique_substrings_single_char():
    """Test single character string"""
    result = find_unique_substrings("a")
    assert result == ["a"]

def test_find_unique_substrings_repeated_chars():
    """Test string with repeated characters"""
    result = find_unique_substrings("aaa")
    assert set(result) == {"a", "aa", "aaa"}

def test_find_unique_substrings_case_sensitivity():
    """Test case sensitivity"""
    result = find_unique_substrings("Ab")
    assert set(result) == {"A", "Ab", "b"}

def test_find_unique_substrings_sorted_output():
    """Test that output is more specifically sorted"""
    result = find_unique_substrings("cba")
    expected_output = sorted(["a", "ab", "b", "c", "bc", "cb", "cba"])
    assert result == expected_output

def test_find_unique_substrings_long_string():
    """Test with a longer string"""
    result = find_unique_substrings("hello")
    # Ensure all character-based and multi-character substrings are captured
    expected_substrings = {
        "h", "he", "hel", "hell", "hello", 
        "e", "el", "ell", "ello", 
        "l", "ll", "llo", 
        "o"
    }
    assert set(result) == expected_substrings
    assert len(result) == len(expected_substrings)