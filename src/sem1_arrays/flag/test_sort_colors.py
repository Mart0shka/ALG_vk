from sort_colors import sort_colors

def test_sort_dutch_flag_empty():
    # Проверка на пустой массив
    arr = []
    sort_colors(arr)
    assert arr == []

def test_sort_dutch_flag_all_zeros():
    # Проверка на массив из нулей
    arr = [0, 0, 0]
    sort_colors(arr)
    assert arr == [0, 0, 0]

def test_sort_dutch_flag_all_ones():
    # Проверка на массив из единиц
    arr = [1, 1, 1]
    sort_colors(arr)
    assert arr == [1, 1, 1]

def test_sort_dutch_flag_all_twos():
    # Проверка на массив из двоек
    arr = [2, 2, 2]
    sort_colors(arr)
    assert arr == [2, 2, 2]

def test_sort_dutch_flag_simple():
    # Проверка на простой случай
    arr = [2, 0, 1, 2, 1, 0]
    sort_colors(arr)
    assert arr == [0, 0, 1, 1, 2, 2]

def test_sort_dutch_flag_already_sorted():
    # Проверка на уже отсортированный массив
    arr = [0, 0, 1, 1, 2, 2]
    sort_colors(arr)
    assert arr == [0, 0, 1, 1, 2, 2]

def test_sort_dutch_flag_reverse_sorted():
    # Проверка на массив, отсортированный в обратном порядке
    arr = [2, 2, 1, 1, 0, 0]
    sort_colors(arr)
    assert arr == [0, 0, 1, 1, 2, 2]

def test_sort_dutch_flag_mixed():
    # Проверка на смешанный массив
    arr = [1, 0, 2, 1, 0, 2]
    sort_colors(arr)
    assert arr == [0, 0, 1, 1, 2, 2]

def test_sort_dutch_flag_large_array():
    # Проверка на большой массив
    arr = [2] * 500 + [1] * 500 + [0] * 500
    sort_colors(arr)
    assert arr == [0] * 500 + [1] * 500 + [2] * 500

def test_sort_dutch_flag_single_zero():
    # Проверка на массив с одним нулём
    arr = [0]
    sort_colors(arr)
    assert arr == [0]

def test_sort_dutch_flag_single_one():
    # Проверка на массив с одной единицей
    arr = [1]
    sort_colors(arr)
    assert arr == [1]

def test_sort_dutch_flag_single_two():
    # Проверка на массив с одной двойкой
    arr = [2]
    sort_colors(arr)
    assert arr == [2]