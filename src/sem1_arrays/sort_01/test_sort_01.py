from sort_01 import sort

def test_sort_binary_array_empty():
    # Проверка на пустой массив
    arr = []
    sort(arr)
    assert arr == []

def test_sort_binary_array_all_zeros():
    # Проверка на массив из нулей
    arr = [0, 0, 0]
    sort(arr)
    assert arr == [0, 0, 0]

def test_sort_binary_array_all_ones():
    # Проверка на массив из единиц
    arr = [1, 1, 1]
    sort(arr)
    assert arr == [1, 1, 1]

def test_sort_binary_array_simple():
    # Проверка на простой случай
    arr = [1, 0, 1, 0, 1]
    sort(arr)
    assert arr == [0, 0, 1, 1, 1]

def test_sort_binary_array_already_sorted():
    # Проверка на уже отсортированный массив
    arr = [0, 0, 1, 1]
    sort(arr)
    assert arr == [0, 0, 1, 1]

def test_sort_binary_array_reverse_sorted():
    # Проверка на массив, отсортированный в обратном порядке
    arr = [1, 1, 0, 0]
    sort(arr)
    assert arr == [0, 0, 1, 1]
def test_sort_binary_array_mixed():
    # Проверка на смешанный массив
    arr = [0, 1, 0, 1, 0, 1]
    sort(arr)
    assert arr == [0, 0, 0, 1, 1, 1]

def test_sort_binary_array_large_array():
    # Проверка на большой массив
    arr = [1] * 500 + [0] * 500
    sort(arr)
    assert arr == [0] * 500 + [1] * 500

def test_sort_binary_array_single_zero():
    # Проверка на массив с одним нулём
    arr = [0]
    sort(arr)
    assert arr == [0]

def test_sort_binary_array_single_one():
    # Проверка на массив с одной единицей
    arr = [1]
    sort(arr)
    assert arr == [1]