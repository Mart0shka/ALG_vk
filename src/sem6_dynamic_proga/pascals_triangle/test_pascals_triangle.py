from pascals_triangle import pascal_triangle

def test_zero_rows():
    # Проверка для n = 0 (пустой треугольник)
    assert pascal_triangle(0) == []

def test_single_row():
    # Проверка для n = 1 (первая строка)
    assert pascal_triangle(1) == [[1]]

def test_two_rows():
    # Проверка для n = 2
    assert pascal_triangle(2) == [[1], [1, 1]]

def test_three_rows():
    # Проверка для n = 3
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1]]

def test_four_rows():
    # Проверка для n = 4
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

def test_five_rows():
    # Проверка для n = 5
    assert pascal_triangle(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]

def test_six_rows():
    # Проверка для n = 6
    assert pascal_triangle(6) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1]
    ]
