from find_max_len import find_max_length

def test_find_max_length_equal_zeros_ones():
    nums = [0, 1]
    assert find_max_length(nums) == 2

def test_find_max_length_multiple_subarrays():
    nums = [0, 1, 0, 1]
    assert find_max_length(nums) == 4

def test_find_max_length_large_equal():
    nums = [1, 0, 1, 0, 1, 0]
    assert find_max_length(nums) == 6

def test_find_max_length_all_zeros():
    nums = [0, 0, 0, 0]
    assert find_max_length(nums) == 0

def test_find_max_length_all_ones():
    nums = [1, 1, 1, 1]
    assert find_max_length(nums) == 0

def test_find_max_length_no_long_equal_subarray():
    nums = [1, 0, 1, 1, 0, 1, 0]
    assert find_max_length(nums) == 6


