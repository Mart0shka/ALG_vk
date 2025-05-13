from pivot_index import pivot_index

def test_pivot_index_exists():
    nums = [1, 7, 3, 6, 5, 6]
    assert pivot_index(nums) == 3

def test_pivot_index_not_found():
    nums = [1, 2, 3]
    assert pivot_index(nums) == -1

def test_pivot_index_same_elements():
    nums = [2, 2, 2, 2, 2]
    assert pivot_index(nums) == 2

def test_pivot_index_no_equal_sum():
    nums = [1, 2, 3, 4]
    assert pivot_index(nums) == -1

def test_pivot_index_last_element():
    nums = [1, 1, 1, 1, 1, 1, 1]
    assert pivot_index(nums) == 3
