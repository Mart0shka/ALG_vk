from shell_sort import shell_sort  # Импортируем тестируемую функцию


def test_empty_list():
    # Проверка пустого списка
    assert shell_sort([]) == []


def test_single_element():
    # Проверка списка с одним элементом
    assert shell_sort([1]) == [1]
    assert shell_sort(["a"]) == ["a"]


def test_sorted_input():
    # Проверка уже отсортированного списка
    assert shell_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert shell_sort(["a", "b", "c"]) == ["a", "b", "c"]


def test_unsorted_numbers():
    # Проверка сортировки чисел
    assert shell_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert shell_sort([10, -5, 0, 15]) == [-5, 0, 10, 15]


def test_unsorted_strings():
    # Проверка сортировки строк
    assert shell_sort(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]
    assert shell_sort(["z", "a", "m"]) == ["a", "m", "z"]


def test_duplicates():
    # Проверка обработки дубликатов
    assert shell_sort([2, 1, 2, 3]) == [1, 2, 2, 3]
    assert shell_sort(["a", "c", "a", "b"]) == ["a", "a", "b", "c"]


def test_large_list():
    # Проверка большой коллекции (100 элементов)
    import random
    test_list = random.sample(range(1, 101), 100)
    assert shell_sort(test_list) == list(range(1, 101))




