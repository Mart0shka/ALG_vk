from merge_with_zero import merge

def test_merge_both_empty():
    # Проверка на два пустых массива
    assert merge([], []) == []

def test_merge_first_empty():
    # Проверка, если первый массив пустой
    assert merge([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_merge_second_empty():
    # Проверка, если второй массив пустой
    assert merge([1, 2, 3], []) == [1, 2, 3]

def test_merge_simple():
    # Проверка на два простых массива
    assert merge([3, 8, 10, 11, 0, 0, 0], [1, 7, 9]) == [1, 3, 7, 8, 9, 10, 11]

def test_merge_duplicates():
    # Проверка на массивы с дублирующими элементами
    assert merge([1, 3, 3, 5, 0, 0, 0], [2, 3, 4]) == [1, 2, 3, 3, 3, 4, 5]

def test_merge_negative_numbers():
    # Проверка на массивы с отрицательными числами
    assert merge([-5, -3, 0, 0, 0, 0], [-4, 1, 2]) == [-5, -4, -3, 0, 1, 2]

def test_merge_large_arrays():
    # Проверка на большие массивы
    arr1 = list(range(0, 100, 2)) + [0] * 50  # Чётные числа: 0, 2, 4, ..., 98 и 50 нулей
    arr2 = list(range(1, 100, 2))  # Нечётные числа: 1, 3, 5, ..., 99
    assert merge(arr1, arr2) == list(range(100))

def test_merge_one_element_each():
    # Проверка на массивы с одним элементом
    assert merge([1, 0], [2]) == [1, 2]

def test_merge_mixed_numbers():
    # Проверка на массивы с положительными и отрицательными числами
    assert merge([-3, 0, 2, 0, 0, 0], [-1, 1, 5]) == [-3, -1, 0, 1, 2, 5]

def test_merge_all_negative_numbers():
    # Проверка на массивы с отрицательными числами
    assert merge([-5, -4, -3, 0, 0], [-2, -1]) == [-5, -4, -3, -2, -1]
