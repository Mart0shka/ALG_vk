from copy_time import copy_time

def test_zero_copies():
    # Проверка случая, когда копий не нужно
    assert copy_time(0, 1, 2) == -1

def test_one_copy():
    # Проверка создания одной копии
    assert copy_time(1, 1, 5) == 1  # Используем быстрый ксерокс
    assert copy_time(1, 3, 2) == 2  # Используем второй ксерокс

def test_both_xeroxes_used():
    # Проверка использования обоих ксероксов
    assert copy_time(5, 1, 2) == 4
    assert copy_time(10, 3, 5) == 21

def test_equal_xeroxes():
    # Проверка случая с одинаковыми ксероксами
    assert copy_time(5, 2, 2) == 6
    assert copy_time(7, 3, 3) == 12

