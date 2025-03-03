from merge import merge_sorted_arrays

def test_merge_sorted_arrays_both_empty():
    # Проверка на два пустых массива
    arr1 = []
    arr2 = []
    result = merge_sorted_arrays(arr1, arr2)
    assert result == []

def test_merge_sorted_arrays_first_empty():
    # Проверка, если первый массив пустой
    arr1 = []
    arr2 = [1, 2, 3]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3]

def test_merge_sorted_arrays_second_empty():
    # Проверка, если второй массив пустой
    arr1 = [1, 2, 3]
    arr2 = []
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3]

def test_merge_sorted_arrays_simple():
    # Проверка на два простых массива
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_arrays_duplicates():
    # Проверка на массивы с дублирующими элементами
    arr1 = [1, 3, 3, 5]
    arr2 = [2, 3, 4]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2, 3, 3, 3, 4, 5]

def test_merge_sorted_arrays_negative_numbers():
    # Проверка на массивы с отрицательными числами
    arr1 = [-5, -3, 0]
    arr2 = [-4, 1, 2]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [-5, -4, -3, 0, 1, 2]

def test_merge_sorted_arrays_large_arrays():
    # Проверка на большие массивы
    arr1 = list(range(0, 100, 2))  # Чётные числа: 0, 2, 4, ..., 98
    arr2 = list(range(1, 100, 2))  # Нечётные числа: 1, 3, 5, ..., 99
    result = merge_sorted_arrays(arr1, arr2)
    assert result == list(range(100))

def test_merge_sorted_arrays_one_element_each():
    # Проверка на массивы с одним элементом
    arr1 = [1]
    arr2 = [2]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [1, 2]

def test_merge_sorted_arrays_mixed_numbers():
    # Проверка на массивы с положительными и отрицательными числами
    arr1 = [-3, 0, 2]
    arr2 = [-1, 1, 5]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [-3, -1, 0, 1, 2, 5]

def test_merge_sorted_arrays_all_negative_numbers():
    # Проверка на массивы с отрицательными числами
    arr1 = [-5, -4, -3]
    arr2 = [-2, -1]
    result = merge_sorted_arrays(arr1, arr2)
    assert result == [-5, -4, -3, -2, -1]