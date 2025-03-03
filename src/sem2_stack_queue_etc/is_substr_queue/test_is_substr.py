from is_substr import is_substr

def test_is_substr_empty_strings_both_empty():
    # Проверка, если обе строки пустые
    assert is_substr("", "") == True

def test_is_substr_empty_strings_a_empty():
    # Проверка, если строка a пустая, а b — нет
    assert is_substr("", "abc") == True

def test_is_substr_empty_strings_b_empty():
    # Проверка, если строка b пустая, а a — нет
    assert is_substr("abc", "") == False

def test_is_substr_same_strings():
    # Проверка, если строки одинаковые
    assert is_substr("abc", "abc") == True

def test_is_substr_valid_subsequence_1():
    assert is_substr("abc", "axbycz") == True

def test_is_substr_valid_subsequence_2():
    assert is_substr("abc", "abxc") == True

def test_is_substr_valid_subsequence_3():
    assert is_substr("abc", "aabbcc") == True

def test_is_substr_invalid_subsequence_1():
    assert is_substr("abc", "acb") == False

def test_is_substr_invalid_subsequence_2():
    assert is_substr("abc", "ab") == False

def test_is_substr_invalid_subsequence_3():
    assert is_substr("abc", "def") == False

def test_is_substr_duplicate_characters_1():
    assert is_substr("aabbcc", "aaabbbccc") == True

def test_is_substr_duplicate_characters_2():
    assert is_substr("aabbcc", "abcabc") == False

def test_is_substr_long_strings_1():
    assert is_substr("abcdef", "axbxcxdxexfx") == True

def test_is_substr_long_strings_2():
    assert is_substr("abcdef", "abdef") == False