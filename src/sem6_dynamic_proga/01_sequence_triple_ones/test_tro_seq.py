from tro_seq import tro_seq

def test_tro_seq_length_0():
    # Проверка для пустой последовательности
    assert tro_seq(0) == 1

def test_tro_seq_length_1():
    # Проверка для последовательности длины 1
    assert tro_seq(1) == 2

def test_tro_seq_length_2():
    # Проверка для последовательности длины 2
    assert tro_seq(2) == 4

def test_tro_seq_length_3():
    # Проверка для последовательности длины 3
    assert tro_seq(3) == 7

def test_tro_seq_length_4():
    # Проверка для последовательности длины 4
    assert tro_seq(4) == 13

def test_tro_seq_length_5():
    # Проверка для последовательности длины 5
    assert tro_seq(5) == 24