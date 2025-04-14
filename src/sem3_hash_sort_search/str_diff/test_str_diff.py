from str_diff import str_diff  # Импортируем тестируемую функцию

def test_empty_string():
    # Проверка пустых строк
    assert str_diff("", "a") == "a"

def test_single_addition():
    # Проверка добавления одного символа
    assert str_diff("abcd", "abcde") == "e"
    assert str_diff("abc", "abdc") == "d"

def test_duplicate_letters():
    # Проверка с дублирующимися буквами
    assert str_diff("aabbcc", "aabbccc") == "c"
    assert str_diff("xxyyzz", "xxyyyzz") == "y"


def test_special_chars():
    # Проверка специальных символов
    assert str_diff("!@#", "!@#$") == "$"
    assert str_diff("123", "1234") == "4"

def test_long_strings():
    # Проверка длинных строк
    assert str_diff("abcdefghijklmnopqrstuvwxyz",
                   "abcdefghijkklmnopqrstuvwxyz") == "k"

