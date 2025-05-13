from find_lis import find_lis

def test_empty_array():
    # Проверка на пустой массив
    assert find_lis([]) == 0

def test_single_element():
    # Проверка на массив из одного элемента
    assert find_lis([5]) == 1

def test_all_equal_elements():
    # Проверка на все одинаковые элементы
    assert find_lis([8, 8, 8, 8]) == 1

def test_strictly_increasing():
    # Проверка на строго возрастающую последовательность
    assert find_lis([1, 2, 3, 4, 5]) == 5

def test_strictly_decreasing():
    # Проверка на строго убывающую последовательность
    assert find_lis([5, 4, 3, 2, 1]) == 1

def test_example_1():
    # Проверка на примере из условия [3, 2, 8, 9, 5, 10]
    assert find_lis([3, 2, 8, 9, 5, 10]) == 3

def test_example_2():
    # Проверка на примере из условия [1, 2, 7, 9, 0, 10]
    assert find_lis([1, 2, 7, 9, 0, 10]) == 4
