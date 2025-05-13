from zo_sequence import zo_seq
from rec_zo_sequence import rec_zo_seq

def test_zo_seq_length_1():
    # Проверка для последовательности длины 1
    assert zo_seq(1) == 2

def test_rec_zo_seq_length_1():
    # Проверка для рекурсивной версии (длина 1)
    assert rec_zo_seq(1) == 2

def test_zo_seq_length_2():
    # Проверка для последовательности длины 2
    assert zo_seq(2) == 3

def test_rec_zo_seq_length_2():
    # Проверка для рекурсивной версии (длина 2)
    assert rec_zo_seq(2) == 3

def test_zo_seq_length_3():
    # Проверка для последовательности длины 3
    assert zo_seq(3) == 5

def test_rec_zo_seq_length_3():
    # Проверка для рекурсивной версии (длина 3)
    assert rec_zo_seq(3) == 5

def test_zo_seq_length_5():
    # Проверка для последовательности длины 5
    assert zo_seq(5) == 13

def test_rec_zo_seq_length_5():
    # Проверка для рекурсивной версии (длина 5)
    assert rec_zo_seq(5) == 13

def test_zo_seq_length_10():
    # Проверка для последовательности длины 10
    assert zo_seq(10) == 144

def test_rec_zo_seq_length_10():
    # Проверка для рекурсивной версии (длина 10)
    assert rec_zo_seq(10) == 144
