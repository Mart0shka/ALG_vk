from src.sem5_cuchi.is_max_heap.is_max_heap import is_max_heap

def test_empty_array():
    assert is_max_heap([]) == True

def test_single_element():
    assert is_max_heap([10]) == True

def test_valid_max_heap():
    #        9
    #       / \
    #      5   3
    #     / \
    #    1   4
    assert is_max_heap([9, 5, 3, 1, 4]) == True

def test_invalid_max_heap():
    #        5
    #       / \
    #      9   3
    assert is_max_heap([5, 9, 3]) == False

def test_valid_max_heap_with_duplicates():
    #        8
    #       / \
    #      8   5
    assert is_max_heap([8, 8, 5]) == True

def test_invalid_max_heap_deep():
    #        10
    #       /  \
    #      5    9
    #     / \
    #    6   3  # 6 > 5 (нарушение)
    assert is_max_heap([10, 5, 9, 6, 3]) == False


def test_invalid_max_heap_right_child():
    #        10
    #       /  \
    #      5    15  # 15 > 10
    assert is_max_heap([10, 5, 15]) == False


def test_large_valid_heap():
    #          100
    #        /     \
    #      99      98
    #     /  \    /  \
    #    97  96 95  94
    assert is_max_heap([100, 99, 98, 97, 96, 95, 94]) == True