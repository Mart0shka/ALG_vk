from max_palindrom import longest_palindrome
from max_palindrom_dp import longest_palindrome_dp

def test_empty_string():
    assert longest_palindrome("") == ""
    assert longest_palindrome_dp("") == ""

def test_single_character():
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("z") == "z"
    assert longest_palindrome_dp("a") == "a"
    assert longest_palindrome_dp("z") == "z"

def test_two_identical_characters():
    assert longest_palindrome("aa") == "aa"
    assert longest_palindrome("bb") == "bb"
    assert longest_palindrome_dp("aa") == "aa"
    assert longest_palindrome_dp("bb") == "bb"

def test_even_length_palindrome():
    assert longest_palindrome("abba") == "abba"
    assert longest_palindrome("noon") == "noon"
    assert longest_palindrome("deed") == "deed"
    assert longest_palindrome_dp("abba") == "abba"
    assert longest_palindrome_dp("noon") == "noon"
    assert longest_palindrome_dp("deed") == "deed"


def test_multiple_palindromes():
    assert longest_palindrome("babad") == "bab" or longest_palindrome("babad") == "aba"
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("aacabdkacaa") == "aca"

    assert longest_palindrome_dp("babad") == "bab" or longest_palindrome_dp("babad") == "aba"
    assert longest_palindrome_dp("cbbd") == "bb"
    assert longest_palindrome_dp("aacabdkacaa") == "aca"
