from coin_change import coin_сhange
from coin_change_dp import coin_сhange_dp
from rec_coin_change import rec_coin_change


def test_coin_change_basic():
    # Базовые тесты для dp версии
    assert coin_сhange_dp([1, 2, 5], 11) == 3
    assert coin_сhange_dp([2, 3, 5], 8) == 2
    assert coin_сhange_dp([1, 3, 4], 6) == 2
    assert coin_сhange_dp([1, 5, 10], 12) == 3
    assert coin_сhange_dp([2, 5], 11) == 4


def test_coin_change_edge_cases():
    # Крайние случаи для dp версии
    assert coin_сhange_dp([1, 2, 5], 0) == 0
    assert coin_сhange_dp([], 0) == 0
    assert coin_сhange_dp([], 5) == -1
    assert coin_сhange_dp([2], 3) == -1
    assert coin_сhange_dp([3], 9) == 3


def test_rec_coin_change_simple():
    # Простые тесты для рекурсивной версии
    assert rec_coin_change([1, 2, 5], 5) == 1
    assert rec_coin_change([1, 3], 4) == 2
    assert rec_coin_change([1, 2], 3) == 2
    assert rec_coin_change([2], 1) == -1


def test_cached_coin_change():
    # Тесты для версии с кешированием
    cache = {}
    assert coin_сhange([1, 2, 5], 5, cache) == 1
    assert 5 in cache

    cache = {}
    assert coin_сhange([1, 3, 4], 6, cache) == 2  # 3 + 3
    assert 6 in cache and 3 in cache



def test_large_amount():
    # Тест с большим amount
    assert coin_сhange_dp([1, 2, 5], 100) == 20  # 20 * 5
    assert coin_сhange_dp([1, 5, 10], 27) == 5  # 10*2 + 5*1 + 1*2

