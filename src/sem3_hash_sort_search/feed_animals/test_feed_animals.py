from feed_animals import feed_animals  # Импортируем тестируемую функцию

def test_empty_animals():
    # Проверка на пустой список животных
    assert feed_animals([], [1, 2, 3]) == 0
    assert feed_animals([], []) == 0

def test_empty_food():
    # Проверка когда нет еды
    assert feed_animals([1, 2, 3], []) == 0
    assert feed_animals([8, 4], []) == 0

def test_single_animal():
    # Проверка одного животного
    assert feed_animals([3], [1, 2, 3]) == 1
    assert feed_animals([5], [1, 2, 3]) == 0

def test_exact_matches():
    # Проверка точных совпадений
    assert feed_animals([1, 2, 3], [1, 2, 3]) == 3
    assert feed_animals([4, 4], [4, 4]) == 2

def test_uneven_distribution():
    # Проверка неравномерного распределения
    assert feed_animals([1, 2, 3, 4], [8]) == 1
    assert feed_animals([1, 2, 3, 4], [3, 3]) == 2

def test_large_numbers():
    # Проверка больших чисел
    assert feed_animals([10, 20, 30], [40]) == 1
    assert feed_animals([100, 200], [300]) == 1

def test_duplicates():
    # Проверка дубликатов
    assert feed_animals([2, 2, 2], [2, 2, 2]) == 3
    assert feed_animals([3, 3], [2, 2, 2]) == 0


def test_unsorted_inputs():
    # Проверка неотсортированных входных данных
    assert feed_animals([3, 1, 2], [2, 1, 3]) == 3
    assert feed_animals([4, 2, 8], [8, 2, 4]) == 3

def test_edge_cases():
    # Проверка граничных случаев
    assert feed_animals([1], [1]) == 1
    assert feed_animals([100], [99]) == 0