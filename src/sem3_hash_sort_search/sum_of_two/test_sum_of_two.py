from sum_of_two import sum_of_two

def test_two_sum_sorted_basic():
    # Проверка на простой случай
    nums = [1, 2, 3, 4, 5]
    target = 7
    assert sum_of_two(nums, target) == (1, 4)

def test_two_sum_sorted_no_solution():
    # Проверка, если решения нет
    nums = [1, 2, 3, 4, 5]
    target = 10
    assert sum_of_two(nums, target) is None

def test_two_sum_sorted_negative_numbers():
    # Проверка на массиве с отрицательными числами
    nums = [-5, -3, 0, 1, 4]
    target = -2
    assert sum_of_two(nums, target) == (1, 3)

def test_two_sum_sorted_duplicates():
    # Проверка на массиве с дублирующими элементами
    nums = [1, 2, 2, 3, 4]
    target = 4
    assert sum_of_two(nums, target) == (0, 3)

def test_two_sum_sorted_single_element():
    # Проверка на массиве из одного элемента
    nums = [5]
    target = 5
    assert sum_of_two(nums, target) is None

def test_two_sum_sorted_large_array():
    # Проверка на большом массиве
    nums = list(range(1, 10001))
    target = 19999
    assert sum_of_two(nums, target) == (9998, 9999)

def test_two_sum_sorted_multiple_pairs():
    # Проверка, если есть несколько пар, дающих target
    nums = [1, 2, 3, 4, 5]
    target = 6
    assert sum_of_two(nums, target) == (0, 4)

def test_two_sum_sorted_zero_target():
    # Проверка на target = 0
    nums = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    target = 0
    assert sum_of_two(nums, target) == (0, 8)
