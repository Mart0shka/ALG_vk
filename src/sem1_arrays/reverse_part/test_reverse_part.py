from reverse_part import solution


def test_rotate_array_single_element():
    # Проверка на массив из одного элемента
    nums = [1]
    solution(nums, 3)
    assert nums == [1]

def test_rotate_array_k_less_than_length():
    # Проверка на массив с k < длины массива
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

def test_rotate_array_k_equal_length():
    # Проверка на массив с k = длине массива
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution(nums, 7)
    assert nums == [1, 2, 3, 4, 5, 6, 7]

def test_rotate_array_k_greater_than_length():
    # Проверка на массив с k > длины массива
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution(nums, 10)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_rotate_array_duplicates():
    # Проверка на массив с дублирующими элементами
    nums = [1, 2, 2, 3, 4, 5, 5]
    solution(nums, 3)
    assert nums == [4, 5, 5, 1, 2, 2, 3]

def test_rotate_array_large_array():
    # Проверка на большой массив
    nums = list(range(1, 10001))
    k = 500
    expected = list(range(9501, 10001)) + list(range(1, 9501))
    solution(nums, k)
    assert nums == expected

def test_rotate_array_all_negative_numbers():
    # Проверка на массив с отрицательными числами
    nums = [-5, -4, -3, -2, -1]
    solution(nums, 2)
    assert nums == [-2, -1, -5, -4, -3]

def test_rotate_array_mixed_numbers():
    # Проверка на массив с положительными и отрицательными числами
    nums = [-3, 0, 2, 5, -1]
    solution(nums, 3)
    assert nums == [2, 5, -1, -3, 0]