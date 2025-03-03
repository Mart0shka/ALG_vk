from even_first import even_first

def test_move_evens_to_front_empty():
    # Проверка на пустой массив
    arr = []
    even_first(arr)
    assert arr == []

def test_move_evens_to_front_no_evens():
    # Проверка на массив без чётных чисел
    arr = [1, 3, 5, 7]
    even_first(arr)
    assert arr == [1, 3, 5, 7]

def test_move_evens_to_front_all_evens():
    # Проверка на массив из чётных чисел
    arr = [2, 4, 6, 8]
    even_first(arr)
    assert arr == [2, 4, 6, 8]

def test_move_evens_to_front_simple():
    # Проверка на простой случай
    arr = [3, 2, 4, 1, 11, 8, 9]
    even_first(arr)
    assert arr == [2, 4, 8, 1, 11, 3, 9]


def test_move_evens_to_front_mixed():
    # Проверка на смешанный массив
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    even_first(arr)
    assert arr == [2, 4, 6, 8, 5, 3, 7, 1]

def test_move_evens_to_front_single_even():
    # Проверка на массив с одним чётным числом
    arr = [1, 3, 2, 5]
    even_first(arr)
    assert arr == [2, 3, 1, 5]


def test_move_evens_to_front_negative_numbers():
    # Проверка на массив с отрицательными числами
    arr = [-3, -2, -4, -1, -11, -8, -9]
    even_first(arr)
    assert arr == [-2, -4, -8, -1, -11, -3, -9]