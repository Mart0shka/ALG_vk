from subarr_sum import subarray_sum

def test_subarray_sum_basic():
    nums = [1, 1, 1]
    k = 2
    assert subarray_sum(nums, k) == 2

def test_subarray_sum_negative_numbers():
    nums = [1, -1, 0]
    k = 0
    assert subarray_sum(nums, k) == 3

def test_subarray_sum_single_match():
    nums = [5]
    k = 5
    assert subarray_sum(nums, k) == 1

def test_subarray_sum_single_fail():
    nums = [4]
    k = 5
    assert subarray_sum(nums, k) == 0

