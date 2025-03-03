from is_palindrome import is_palindrome

def test_is_palindrome_empty_string():
    # Проверка на пустую строку
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    # Проверка на строку из одного символа
    assert is_palindrome("a") == True

def test_is_palindrome_simple_palindrome():
    # Проверка на простой палиндром
    assert is_palindrome("racecar") == True

def test_is_palindrome_simple_not_palindrome():
    # Проверка на строку, которая не является палиндромом
    assert is_palindrome("hello") == False

def test_is_palindrome_numbers():
    # Проверка на палиндром с числами
    assert is_palindrome("12321") == True

def test_is_palindrome_numbers_not_palindrome():
    # Проверка на числа, которые не являются палиндромом
    assert is_palindrome("12345") == False