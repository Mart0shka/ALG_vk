from max_benefit import max_benefit

def test_empty_prices():
    # Проверка на пустой массив
    assert max_benefit([]) == 0

def test_single_price():
    # Проверка на массив с одной ценой
    assert max_benefit([5]) == 0

def test_two_prices_profit():
    # Проверка на две цены с прибылью
    assert max_benefit([1, 5]) == 4

def test_two_prices_no_profit():
    # Проверка на две цены без прибыли
    assert max_benefit([5, 1]) == 0

def test_all_decreasing():
    # Проверка на постоянно падающие цены
    assert max_benefit([5, 4, 3, 2, 1]) == 0

def test_all_increasing():
    # Проверка на постоянно растущие цены
    assert max_benefit([1, 2, 3, 4, 5]) == 4

def test_multiple_peaks():
    # Проверка на несколько пиков
    assert max_benefit([3, 1, 5, 2, 6, 4]) == 5

def test_flat_prices():
    # Проверка на одинаковые цены
    assert max_benefit([2, 2, 2, 2]) == 0
