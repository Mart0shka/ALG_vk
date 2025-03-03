from zero_to_end import zero_to_end

def test_move_zeros_to_end_empty():
    # Проверка на пустой массив
    arr = []
    zero_to_end(arr)
    assert arr == []

def test_move_zeros_to_end_no_zeros():
    # Проверка на массив без нулей
    arr = [1, 2, 3, 4, 5]
    zero_to_end(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_move_zeros_to_end_all_zeros():
    # Проверка на массив из нулей
    arr = [0, 0, 0, 0]
    zero_to_end(arr)
    assert arr == [0, 0, 0, 0]

def test_move_zeros_to_end_simple():
    # Проверка на простой случай
    arr = [3, 0, 2, 0, 1, 0]
    zero_to_end(arr)
    assert arr == [3, 2, 1, 0, 0, 0]

def test_move_zeros_to_end_already_sorted():
    # Проверка на массив, где нули уже в конце
    arr = [1, 2, 3, 0, 0, 0]
    zero_to_end(arr)
    assert arr == [1, 2, 3, 0, 0, 0]

def test_move_zeros_to_end_mixed():
    # Проверка на смешанный массив
    arr = [0, 1, 0, 2, 0, 3, 0]
    zero_to_end(arr)
    assert arr == [1, 2, 3, 0, 0, 0, 0]

def test_move_zeros_to_end_large_array():
    # Проверка на большой массив
    arr = [0] * 500 + [1] * 500 + [0] * 500
    zero_to_end(arr)
    assert arr == [1] * 500 + [0] * 1000

def test_move_zeros_to_end_single_zero():
    # Проверка на массив с одним нулём
    arr = [1, 2, 0, 3]
    zero_to_end(arr)
    assert arr == [1, 2, 3, 0]

def test_move_zeros_to_end_single_non_zero():
    # Проверка на массив с одним ненулевым элементом
    arr = [0, 0, 1, 0]
    zero_to_end(arr)
    assert arr == [1, 0, 0, 0]

def test_move_zeros_to_end_negative_numbers():
    # Проверка на массив с отрицательными числами
    arr = [0, -1, 0, -2, 0, -3]
    zero_to_end(arr)
    assert arr == [-1, -2, -3, 0, 0, 0]