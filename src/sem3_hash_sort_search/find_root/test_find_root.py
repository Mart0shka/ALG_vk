from find_root import find_root  # Импортируем вашу функцию

def test_exact_squares():
    # Проверка точных квадратов
    assert find_root(16) == 4
    assert find_root(25) == 5
    assert find_root(1) == 1
    assert find_root(0) == 0

def test_numbers_between_squares():
    # Проверка чисел между квадратами
    assert find_root(17) == 4
    assert find_root(24) == 4
    assert find_root(10) == 3
    assert find_root(37) == 6

def test_edge_cases():
    # Проверка граничных случаев
    assert find_root(1) == 1
    assert find_root(0) == 0
