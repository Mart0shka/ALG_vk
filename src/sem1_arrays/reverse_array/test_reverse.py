from reverse_array import reverse_array

def test_reverse_array_empty():
    # Проверка на пустой массив
    nums = []
    reverse_array(nums)
    assert nums == []

def test_reverse_array_single_element():
    # Проверка на массив из одного элемента
    nums = [1]
    reverse_array(nums)
    assert nums == [1]

def test_reverse_array_even_length():
    # Проверка на массив чётной длины
    nums = [1, 2, 3, 4]
    reverse_array(nums)
    assert nums == [4, 3, 2, 1]

def test_reverse_array_odd_length():
    # Проверка на массив нечётной длины
    nums = [1, 2, 3, 4, 5]
    reverse_array(nums)
    assert nums == [5, 4, 3, 2, 1]

def test_reverse_array_negative_numbers():
    # Проверка на массив с отрицательными числами
    nums = [-5, -3, 0, 1, 4]
    reverse_array(nums)
    assert nums == [4, 1, 0, -3, -5]

def test_reverse_array_duplicates():
    # Проверка на массив с дублирующими элементами
    nums = [1, 2, 2, 3, 4]
    reverse_array(nums)
    assert nums == [4, 3, 2, 2, 1]

def test_reverse_array_large_array():
    # Проверка на большой массив
    nums = list(range(1, 10001))
    expected = list(range(10000, 0, -1))
    reverse_array(nums)
    assert nums == expected

def test_reverse_array_all_negative_numbers():
    # Проверка на массив с отрицательными числами
    nums = [-5, -4, -3, -2, -1]
    reverse_array(nums)
    assert nums == [-1, -2, -3, -4, -5]

def test_reverse_array_mixed_numbers():
    # Проверка на массив с положительными и отрицательными числами
    nums = [-3, 0, 2, 5, -1]
    reverse_array(nums)
    assert nums == [-1, 5, 2, 0, -3]
